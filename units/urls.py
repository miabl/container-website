from django.urls import path
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

urlpatterns += [
    path('addunit/', views.UnitCreate.as_view(), name='add-unit'),
]

urlpatterns += [
    path('unit/<pk>/update2/', views.edit_teachers, name='update_teachers'),
]
urlpatterns += [
    path('unit/<pk>/deleteunit/', views.UnitDelete.as_view(), name='delete-unit'),
]

urlpatterns += [
    path('unit/<pk>/updateunit/', views.UnitUpdate.as_view(), name='update-unit'),
]

urlpatterns += [
    path('unit/<pk>/updatetitle/', views.edit_title, name='update-title'),
]

urlpatterns += [
    path('unit/<pk>/updateavailability/', views.edit_availability, name='update-availability'),
]

urlpatterns += [
    path('unit/<pk>/changecontainers/', views.change_containers, name='change-containers'),
]
#
# urlpatterns += [
#     path('unit/<pk>/editenrolment/', views.edit_enrolment, name='edit-enrolment'),
# ]

urlpatterns += [
    path('coordinator', views.TeacherListView.as_view(), name='teacher-list'),
]

urlpatterns += [
    path('coordinator/<pk>', views.UserDetailView.as_view(), name='user-detail'),
]
