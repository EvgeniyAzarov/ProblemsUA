from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    color = models.IntegerField(default=0)

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
    attributes = models.ManyToManyField(Attribute, blank=True)
    parents = models.ManyToManyField('self', blank=True)
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.text[:80] + "..."


class Solution(models.Model):
    text = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)


