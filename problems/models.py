from django.db import models
from colorfield.fields import ColorField


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    COLOR_CHOICES = [
        ("#555B6E", "Independence"),
        ("#89B0AE", "Morning Blue"),
        ("#BEE3DB", "Powder Blue"),
        ("#FAF9F9", "Cultured"),
        ("#FFD6BA", "Apricot")
    ]
    color = ColorField(default='#555B6E', choices=COLOR_CHOICES)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)


class Source(models.Model):
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name}, grade {self.grade} ({self.country}, {self.year})'


class Problem(models.Model):
    name = models.CharField(max_length=255, blank=True,
                            help_text="This field is not necessary")
    text = models.TextField()
    difficulty = models.FloatField(default=10, null=True, blank=True)
    attributes = models.ManyToManyField(Attribute, null=True, blank=True)
    themes = models.ManyToManyField(Theme, null=True, blank=True)
    parents = models.ManyToManyField('self', null=True, blank=True)
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    solution = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.text[:80] + "..."

