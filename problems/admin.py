from django.contrib import admin
from .models import Problem, Attribute, Theme, Source


class ProblemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meta', {
            'classes': ['collapse'],
            'fields': ['source', 'difficulty', 'parents', 'name'],
        }),
        ('Problem', {
            'fields': ['text', 'solution'],
        }),
    ]


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Theme)
admin.site.register(Attribute)
admin.site.register(Source)

