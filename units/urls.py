from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
   #  path('unit/', views.UnitDetailView.as_view(), name='unit-detail'),
   # # path('units/', views.IndexView.as_view(), name='unit'),
]