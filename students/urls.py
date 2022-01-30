from django.urls import path, include
from students import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('student', views.StudentListView.as_view(), name='student-list'),
    # path('student/<pk>', views.StudentDetailView.as_view(), name='student-detail'),
    # path('student/<pk>/addstudent', views.edit_enrolment, name='add-student'),
]
