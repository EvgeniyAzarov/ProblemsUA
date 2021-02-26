from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=100)
    color = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Problem(models.Model):
    task = models.CharField(max_length=100000)
    solution = models.CharField(max_length=100000)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return self.task

