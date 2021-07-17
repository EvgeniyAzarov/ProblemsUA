# Generated by Django 3.1.7 on 2021-07-17 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0008_auto_20210601_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.source'),
        ),
    ]