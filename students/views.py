# Create your views here.
from django.shortcuts import redirect
from .forms import NewUserForm  # , EditStudentsForm
from django.views.generic.edit import UpdateView
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render


# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required


def register(response):
    if response.method == 'POST':
        form = NewUserForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('index')
    else:
        form = NewUserForm()

    return render(response, 'registration/register.html', {'form': form})


class StudentUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'accounts/login'
    model = Student
    fields = ['user', 'units']

    def get_initial(self):
        initial = super(StudentUpdate, self).get_initial()
        initial.update({'user': self.request.user})
        return initial


class StudentListView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts/login/'
    model = Student
    template_name = 'students/student_list.html'


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts/login/'
    model = Student
    template_name = 'students/student_detail.html'

# @login_required
# def edit_enrolment(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#         form = EditStudentsForm(request.POST)
#
#         if form.is_valid():
#             student.units.set(form.cleaned_data['units'])
#             student.save()
#
#             return HttpResponseRedirect(reverse('student-list'))
#     else:
#         proposed_students = ''
#         form = EditStudentsForm(
#             initial={'units': proposed_students, }
#         )
#
#     context = {
#         'form': form,
#         'student': student,
#     }
#     return render(request, 'students/student_form.html', context)
