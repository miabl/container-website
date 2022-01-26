from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit
from students.models import Student
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from units.forms import EditUnitForm, EditTeachersForm, EditTitleForm, EditAvailabilityForm, EditContainersForm

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts/login/'
    model = Unit
    template_name = 'index.html'

    def get_queryset(self):
        uns = Unit.objects.filter(Q(coordinator__user=self.request.user) | Q(
            lecturer__user=self.request.user) | Q(
            lab_facilitator__user=self.request.user))
        try:
            stud = Student.objects.get(user=self.request.user)
            stud_uns = stud.units.all()
            all_units = stud_uns | uns
        except Student.DoesNotExist:
            all_units = uns
        return all_units


class UnitDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts/login/'
    model = Unit
    template_name = 'units/unit_detail.html'


@login_required
@permission_required('units.can_update_unit', raise_exception=True)
def edit_unit(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = EditUnitForm(request.POST)

        if form.is_valid():
            unit.summary = form.cleaned_data['summary']
            unit.save()

            return HttpResponseRedirect(reverse('teaching'))
    else:
        proposed_summary = ""
        form = EditUnitForm(
            initial={'summary': proposed_summary, }
        )

    context = {
        'form': form,
        'unit': unit,
    }

    return render(request, 'units/update_summary.html', context)


@login_required
@permission_required('units.can_update_unit', raise_exception=True)
def edit_teachers(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = EditTeachersForm(request.POST)

        if form.is_valid():
            unit.coordinator = form.cleaned_data['coordinator']
            unit.lecturer.set(form.cleaned_data['lecturer'])
            unit.lab_facilitator.set(form.cleaned_data['lab_facilitator'])
            unit.save()

            return HttpResponseRedirect(reverse('teaching'))
    else:
        proposed_coordinator = ""
        proposed_lecturer = ""
        proposed_lab_facilitator = ""
        form = EditTeachersForm(
            initial={'coordinator': proposed_coordinator, 'lecturer': proposed_lecturer,
                     'lab_facilitator': proposed_lab_facilitator, }
        )

    context = {
        'form': form,
        'unit': unit,
    }

    return render(request, 'units/update_teachers.html', context)


@login_required
@permission_required('units.can_update_unit', raise_exception=True)
def edit_title(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = EditTitleForm(request.POST)

        if form.is_valid():
            unit.title = form.cleaned_data['title']
            unit.save()

            return HttpResponseRedirect(reverse('teaching'))
    else:
        proposed_title = ""
        form = EditTitleForm(
            initial={'title': proposed_title, }
        )

    context = {
        'form': form,
        'unit': unit,
    }

    return render(request, 'units/update_title.html', context)


@login_required
@permission_required('units.can_update_unit', raise_exception=True)
def edit_availability(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = EditAvailabilityForm(request.POST)

        if form.is_valid():
            unit.availability = form.cleaned_data['availability']
            unit.save()

            return HttpResponseRedirect(reverse('teaching'))
    else:
        proposed_availability = 'ns'
        form = EditAvailabilityForm(
            initial={'availability': proposed_availability, }
        )

    context = {
        'form': form,
        'unit': unit,
    }

    return render(request, 'units/update_availability.html', context)


@login_required
@permission_required('units.can_update_unit', raise_exception=True)
def change_containers(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = EditContainersForm(request.POST)

        if form.is_valid():
            unit.containers.set(form.cleaned_data['containers'])
            unit.save()

            return HttpResponseRedirect(reverse('teaching'))
    else:
        proposed_containers = ''
        form = EditContainersForm(
            initial={'containers': proposed_containers, }
        )

    context = {
        'form': form,
        'unit': unit,
    }

    return render(request, 'units/update_containers.html', context)


class AllUnits(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = 'accounts/login/'
    model = Unit
    permission_required = 'units.can_view_all'
    template_name = 'units/unit_list_all.html'
    paginate_by = 10


class UnitCreate(PermissionRequiredMixin, CreateView):
    model = Unit
    permission_required = 'units.can_update_unit'
    fields = '__all__'


class UnitUpdate(PermissionRequiredMixin, UpdateView):
    model = Unit
    permission_required = 'units.can_update_unit'
    fields = '__all__'


class UnitDelete(PermissionRequiredMixin, DeleteView):
    model = Unit
    permission_required = 'units.can_update_unit'
    success_url = reverse_lazy('teaching')
