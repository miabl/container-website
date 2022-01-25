from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit
from students.models import Student
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from units.forms import EditUnitForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts/login/'
    model = Unit
    template_name = 'index.html'

    def get_queryset(self):
        stud = Student.objects.get(user=self.request.user)
        uns = stud.units.all()
        return uns


class UnitDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts/login/'
    model = Unit
    template_name = 'units/unit_detail.html'


@login_required
@permission_required('unit.can_edit_unit', raise_exception=True)
def edit_unit(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = EditUnitForm(request.POST)

        if form.is_valid():
            unit.summary = form.cleaned_data['change_summary']
            unit.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        summary = "hello"
        form = EditUnitForm(initial={'update_summary': summary})

    context = {
        'form': form,
        'unit': unit,
    }

    return render(request, 'units/update_summary.html', context)


# from django.contrib.auth.models import Group
#
#
# def registerTeacher():
#     teacher_group, created = Group.objects.get_or_create(name="COORDINATOR")
#     ct = ContentType.objects.get_for_model(Unit)
#     p


class AllUnits(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Unit
    permission_required = 'unit.can_edit_unit'
    template_name = 'units/unit_list_all.html'
    paginate_by = 10
