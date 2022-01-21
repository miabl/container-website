from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit
from django.shortcuts import render

# def index(request):
#     """View function for home page of site."""
#     all_units = Unit.objects.all()
#     context = {
#         'all_units': all_units,
#     }
#
#     return render(request, 'index.html', context=context)

from django.views import generic
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Unit
    template_name = 'index.html'

# class UnitDetailView(generic.DetailView):
#     model = Unit
#     template_name = 'units/unit_detail.html'

#class UnitList(LoginRequiredMixin, generic.ListView):
#     login_url = '/login/'
#     model = Unit
#     context_object_name = 'unit_list'
#     template_name = 'units/unit-list.html'