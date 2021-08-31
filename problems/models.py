from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from colorfield.fields import ColorField


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    COLOR_CHOICES = [
        ("#9CA7CA", "Independence light"),
        ("#89B0AE", "Morning Blue"),
        ("#BEE3DB", "Powder Blue"),
        ("#FAF9F9", "Cultured"),
        ("#FFD6BA", "Apricot")
    ]
    color = ColorField(default='#555B6E', choices=COLOR_CHOICES)

    def __str__(self):
        return self.name


class Theme(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    class MPPTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        out = f'{self.name}'
        if self.country:
            out += f' ({self.country})'

        return out


class Problem(models.Model):
    name = models.CharField(max_length=255, blank=True,
                            help_text="e.g. butterfly theorem")
    text = models.TextField()
    difficulty = models.FloatField(default=10, null=True, blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)
    parents = models.ManyToManyField('self', blank=True)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.SET_NULL)
    grade = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True,
                                 help_text="Number, under which the problem was proposed")
    solution = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        full_text = ""
        if self.name:
            full_text += f"({self.name}) "
        full_text += self.text
        return f"[{self.id}] " + full_text[:80] + "..."

    class Meta:
        ordering = ['-id']

