# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-01 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bul_cbp_app', '0007_auto_20180225_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='accessability_check_run',
            new_name='accessibility_check_run',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='accessability_check_run_CHECKED',
            new_name='accessibility_check_run_CHECKED',
        ),
    ]
