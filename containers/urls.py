from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ContainerList.as_view(), name="container-list"),
    path('container/<int:pk>', views.ContainerDetail.as_view(), name="container-detail"),
    path('start_container', views.startContainer, name="start-container"),
]
