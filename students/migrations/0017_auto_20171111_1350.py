# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-11 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_studentprogram_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprogram',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Term'),
        ),
    ]
