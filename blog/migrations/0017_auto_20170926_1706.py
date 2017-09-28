# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170926_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waveguide',
            name='amplitude',
            field=models.FloatField(blank=True, help_text='Amplitude of the signal.', null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='frecuency',
            field=models.FloatField(blank=True, help_text='Frequency of the signal.', null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='i_down',
            field=models.FloatField(blank=True, help_text=' Value of the current down.', null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='i_up',
            field=models.FloatField(blank=True, help_text='Value of the current up.', null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='lod',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='noise',
            field=models.FloatField(blank=True, help_text='Noise in the signal.', null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='offset',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='slope',
            field=models.FloatField(blank=True, help_text='Slope of the signal.', null=True),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='visibility',
            field=models.FloatField(blank=True, help_text='Visibility of th e signal.', null=True),
        ),
    ]