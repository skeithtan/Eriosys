# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0009_auto_20171104_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='contact_person_email',
            field=models.CharField(max_length=256, null=True),
        ),
    ]