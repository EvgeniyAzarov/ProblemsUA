# Generated by Django 3.1.7 on 2021-05-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20210527_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='solution',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.FloatField(blank=True, default=10, null=True),
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
    ]