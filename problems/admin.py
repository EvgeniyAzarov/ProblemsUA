from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Problem, Attribute, Theme, Source


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'source',)
    search_fields = ('text', 'name')
    list_filter = (
        ('themes', admin.RelatedFieldListFilter),
    )
    autocomplete_fields = ('source', )
    filter_horizontal = ('attributes', 'themes', 'parents')
    fieldsets = [
        ('Meta', {
            'classes': ['collapse'],
            'fields': ['source', 'difficulty', 'name', 'parents', 'attributes', 'themes'],
        }),
        ('Problem', {
            'fields': ['text', 'solution'],
        }),
    ]


class ThemeAdmin(DjangoMpttAdmin):
    pass


class SourceAdmin(admin.ModelAdmin):
    search_fields = ('name', )


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Attribute)
admin.site.register(Source, SourceAdmin)
