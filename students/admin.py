from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Student
from units.models import Coordinator, Lecturer, LabFacilitator


class StudentInLine(admin.StackedInline):
    model = Student
    can_delete = False
    can_edit_unit = True
    verbose_name_plural = 'student'


class CoordinatorInLine(admin.StackedInline):
    model = Coordinator
    can_delete = False
    verbose_name_plural = 'coordinator'


class LecturerInLine(admin.StackedInline):
    model = Lecturer
    can_delete = False
    verbose_name_plural = 'lecturer'


class LabFacilitatorInLine(admin.StackedInline):
    model = LabFacilitator
    can_delete = False
    can_edit_unit = True
    verbose_name_plural = 'lab_facilitator'


class UserAdmin(BaseUserAdmin):
    inlines = (StudentInLine, CoordinatorInLine, LecturerInLine, LabFacilitatorInLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
