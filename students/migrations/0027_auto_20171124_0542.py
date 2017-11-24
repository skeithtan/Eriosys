# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-24 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0026_auto_20171121_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirement',
            name='program',
        ),
        migrations.AlterField(
            model_name='studentapplicationrequirement',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Requirement'),
        ),
        migrations.DeleteModel(
            name='Requirement',
        ),
    ]