from django.urls import path, include
from . import views

urlpatterns = [
    path('unit/<pk>', views.UnitDetailView.as_view(), name='unit-detail'),
    # path('container/<pk>', views.UnitDetailView.as_view(), name='container_detail'),
]

urlpatterns += [
    path('unit/<pk>/update/', views.edit_unit, name='update_summary'),
]

urlpatterns += [
    path('teaching/', views.AllUnits.as_view(), name='teaching'),
]
