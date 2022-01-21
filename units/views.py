from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Unit


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Unit
    template_name = 'index.html'


class UnitDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Unit
    template_name = 'units/unit_detail.html'
