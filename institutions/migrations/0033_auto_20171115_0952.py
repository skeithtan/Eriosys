# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0032_auto_20171115_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='user',
            new_name='archiver',
        ),
        migrations.RenameField(
            model_name='memorandum',
            old_name='user',
            new_name='archiver',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='user',
            new_name='archiver',
        ),
        migrations.RenameField(
            model_name='studyfield',
            old_name='user',
            new_name='archiver',
        ),
        migrations.RenameField(
            model_name='term',
            old_name='user',
            new_name='archiver',
        ),
    ]
