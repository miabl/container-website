from django.urls import path
from . import views

urlpatterns = [
    path('unit/<pk>', views.UnitDetailView.as_view(), name='unit-detail'),
]
