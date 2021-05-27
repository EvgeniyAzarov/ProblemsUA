from django.contrib import admin
from .models import Problem, Attribute, Solution, Theme, Source


class SolutionInline(admin.StackedInline):
    model = Solution
    extra = 1


class ProblemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meta', {
            'classes': ['collapse'],
            'fields': ['name'],
        }),
        (None, {
            'fields': ['text', 'source'],
        }),

    ]
    inlines = [SolutionInline]


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Theme)
admin.site.register(Attribute)
admin.site.register(Source)

