# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20171103_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='id_number',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
