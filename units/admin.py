from django.contrib import admin

from .models import Unit


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
