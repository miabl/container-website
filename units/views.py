from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit

class UnitList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Unit
    context_object_name = 'unit_list'
    template_name = 'units/unit-list.html'