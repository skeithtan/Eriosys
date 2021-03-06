# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0034_auto_20171117_1010'),
        ('students', '0024_auto_20171117_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('archiver', models.CharField(blank=True, max_length=32)),
                ('default_units', models.PositiveIntegerField()),
                ('total_units_enrolled', models.PositiveIntegerField()),
                ('date_expected_return', models.DateField(null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('study_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.StudyField')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Term')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='studentstudyfield',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentstudyfield',
            name='study_field',
        ),
        migrations.RemoveField(
            model_name='studentstudyfield',
            name='term',
        ),
        migrations.DeleteModel(
            name='StudentStudyField',
        ),
    ]
