from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit

# from containers.models import Container
# from django.contrib.auth.models import User
from students.models import Student


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Unit
    template_name = 'index.html'

    def get_queryset(self):
        stud = Student.objects.get(user=self.request.user)
        uns = stud.units.all()
        return uns


class UnitDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Unit
    template_name = 'units/unit_detail.html'
    # this_student = Student.objects.get(user=request.user)

    #
    # def get_queryset(self):
    #     return Container.objects.filter(unit=Unit)

# from django.shortcuts import render
#
# from django.contrib.auth.decorators import login_required, permission_required
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
#
# from units.forms import EditUnit

# @login_required
# @permission_required('catalog.can_mark_returned', raise_exception=True)
# def edit_unit(request, pk):
#     """View function for renewing a specific BookInstance by librarian."""
#     unit = get_object_or_404(Unit, pk=pk)
#
#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#
#         # Create a form instance and populate it with data from the request (binding):
#         form = EditUnit(request.POST)
#
#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             unit.due_back = form.cleaned_data['change_title']
#             unit.save()
#
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('index'))
#
#     # If this is a GET (or any other method) create the default form.
#     else:
#         proposed_change_name = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
#
#     context = {
#         'form': form,
#         'book_instance': book_instance,
#     }
#
#     return render(request, 'catalog/book_renew_librarian.html', context)
