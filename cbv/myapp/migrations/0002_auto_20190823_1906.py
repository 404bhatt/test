# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-08-23 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='myapp.school'),
        ),
    ]
