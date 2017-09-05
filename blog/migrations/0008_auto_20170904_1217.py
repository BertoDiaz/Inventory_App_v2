# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170904_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waveguide',
            name='amplitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='frecuency',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='i_down',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='i_up',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='lod',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='noise',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='offset',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='slope',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='visibility',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='waveguide',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Name_Waveguide'),
        ),
    ]
