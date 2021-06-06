# Generated by Django 3.1.7 on 2021-06-01 15:34

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0007_auto_20210528_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='source',
            name='year',
        ),
        migrations.AddField(
            model_name='problem',
            name='grade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#9CA7CA', 'Independence light'), ('#89B0AE', 'Morning Blue'), ('#BEE3DB', 'Powder Blue'), ('#FAF9F9', 'Cultured'), ('#FFD6BA', 'Apricot')], default='#555B6E', max_length=18),
        ),
    ]
