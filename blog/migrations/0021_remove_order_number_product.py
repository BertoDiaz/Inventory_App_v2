# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20171107_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number_product',
        ),
    ]