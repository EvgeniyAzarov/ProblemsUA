# Generated by Django 3.1.7 on 2021-03-18 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('problems', '0001_initial'), ('problems', '0002_auto_20210226_0001'), ('problems', '0003_auto_20210226_0003'), ('problems', '0004_auto_20210317_1829'), ('problems', '0005_auto_20210317_1829'), ('problems', '0006_auto_20210317_1845'), ('problems', '0007_auto_20210317_2231'), ('problems', '0008_auto_20210317_2231')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('attributes', models.ManyToManyField(blank=True, to='problems.Attribute')),
                ('difficulty', models.FloatField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('parents', models.ManyToManyField(blank=True, related_name='_problem_parents_+', to='problems.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
            ],
        ),
    ]
