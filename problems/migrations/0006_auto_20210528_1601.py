# Generated by Django 3.1.7 on 2021-05-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_auto_20210528_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='themes',
        ),
        migrations.AlterField(
            model_name='problem',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='problems.Attribute'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='_problem_parents_+', to='problems.Problem'),
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
    ]
