# Generated by Django 3.1.7 on 2021-05-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20210527_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]