from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContainerList.as_view(), name="container-list"),
    path('container/<int:pk>', views.ContainerDetail.as_view(), name="container-detail"),
    path('start-container/<int:container_pk>', views.StartContainer.as_view(), name="start-container"),
    path('failure', views.FailedContainer.as_view(), name='failure'),
    path('container-instance/<int:pk>/', views.ContainerInstanceDetail.as_view(), name='container-instance-detail'),
]
