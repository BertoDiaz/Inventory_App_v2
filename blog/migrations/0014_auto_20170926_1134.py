# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170926_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='chip',
            field=models.CharField(help_text='ID of the chip.', max_length=50),
        ),
    ]
