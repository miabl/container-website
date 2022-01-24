from django.contrib import admin

from .models import Unit, Coordinator, Lecturer, LabFacilitator


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'availability', 'coordinator')
    list_filter = ('availability', 'coordinator')
    fieldsets = (
        (None, {
            'fields': ('title', 'code')
        }),
        ('Staff', {
            'fields': ('coordinator', 'lecturer', 'lab_facilitator')
        }),
        ('Details', {
            'fields': ('summary', 'availability', 'containers')
        }),
    )
    pass


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name')
    fields = ['user', ('title', 'first_name'), 'last_name']
    pass


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name')
    pass


@admin.register(LabFacilitator)
class LabFacilitatorAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name')
    pass
