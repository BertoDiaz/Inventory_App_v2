# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 09:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20170919_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the inventory.', max_length=200)),
                ('maker', models.CharField(help_text='Manufacturer of the inventory.', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.')),
                ('author', models.ForeignKey(help_text='Name of the author that created the inventory.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='element',
            name='author',
        ),
        migrations.RemoveField(
            model_name='element',
            name='type_item',
        ),
        migrations.AlterField(
            model_name='chip',
            name='date',
            field=models.DateField(blank=True, help_text='When was took.'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='user_name',
            field=models.ForeignKey(blank=True, help_text='Who have the chip.', on_delete=django.db.models.deletion.CASCADE, to='blog.Full_Name_Users'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(help_text='Name of the type of inventory.', max_length=200),
        ),
        migrations.DeleteModel(
            name='Element',
        ),
        migrations.AddField(
            model_name='inventory',
            name='type_item',
            field=models.ForeignKey(help_text='Type of inventory.', on_delete=django.db.models.deletion.CASCADE, to='blog.Type'),
        ),
    ]