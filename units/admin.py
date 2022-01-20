from django.contrib import admin

from .models import Unit, Coordinator, Lecturer, lab_facilitator

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    pass

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    pass

@admin.register(lab_facilitator)
class lab_facilitatorAdmin(admin.ModelAdmin):
    pass