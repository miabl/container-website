from django.urls import path
from . import views

urlpatterns = [
    path('', views.UnitList.as_view(), name="unit-list"),
]