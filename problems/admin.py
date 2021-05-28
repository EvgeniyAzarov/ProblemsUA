from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Problem, Attribute, Theme, Source


class ProblemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meta', {
            'classes': ['collapse'],
            'fields': ['source', 'difficulty', 'parents', 'name', 'attributes', 'themes'],
        }),
        ('Problem', {
            'fields': ['text', 'solution'],
        }),
    ]


class ThemeAdmin(DjangoMpttAdmin):
    pass


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Attribute)
admin.site.register(Source)
