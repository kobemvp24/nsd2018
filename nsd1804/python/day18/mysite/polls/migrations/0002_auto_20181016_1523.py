# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-16 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='q',
        ),
    ]