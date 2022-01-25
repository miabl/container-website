from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit
from students.models import Student
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from units.forms import EditUnitForm, EditTeachersForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.db.models import Q

from django.views.generic.edit import CreateView, DeleteView
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
            unit.title = form.cleaned_data['title']
            unit.availability = form.cleaned_data['availability']
            unit.save()

            return HttpResponseRedirect(reverse('teaching'))
    else:
        proposed_summary = ""
        proposed_title = ""
        proposed_availability = 'ns'
        form = EditUnitForm(
            initial={'title': proposed_title, 'summary': proposed_summary,
                     'availability': proposed_availability, }
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


class AllUnits(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = 'accounts/login/'
    model = Unit
    permission_required = 'units.can_view_all'
    template_name = 'units/unit_list_all.html'
    paginate_by = 10


class UnitCreate(CreateView):
    model = Unit
    fields = '__all__'


class UnitDelete(DeleteView):
    model = Unit
    success_url = reverse_lazy('teaching')
