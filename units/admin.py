from django.contrib import admin

from .models import Unit, Coordinator, Lecturer, lab_facilitator

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'availability', 'coordinator')
    list_filter = ('availability', 'coordinator')
    fieldsets = (
        (None, {
            'fields': ('title', 'code')
        }),
        ('Staff', {
            'fields': ('coordinator', 'lecturer','lab_facilitator')
        }),
        ('Details', {
            'fields': ('summary', 'availability')
        }),
    )
    pass

@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('title','first_name', 'last_name')
    fields = [('title', 'first_name'), 'last_name']
    pass

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('title','first_name', 'last_name')
    pass

@admin.register(lab_facilitator)
class lab_facilitatorAdmin(admin.ModelAdmin):
    list_display = ('title','first_name', 'last_name')
    pass