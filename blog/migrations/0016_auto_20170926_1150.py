# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170926_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='user_name',
            field=models.ForeignKey(blank=True, help_text='Who have the chip.', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Full_Name_Users'),
        ),
    ]
