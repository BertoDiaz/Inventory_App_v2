# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170914_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biological',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of the biological component.', max_length=200)),
                ('reference', models.CharField(blank=True, help_text='Reference of the biological component.', max_length=200)),
                ('quantity', models.CharField(help_text='Quantity of the biological component.', max_length=20)),
                ('concentration', models.CharField(blank=True, help_text='Concentration of the biological component.', max_length=200)),
                ('molecular_weight', models.CharField(blank=True, help_text='Molecular weight of the biological component.', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.')),
            ],
        ),
        migrations.CreateModel(
            name='Type_Biological',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the type of biological component.', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.')),
            ],
        ),
        migrations.AlterField(
            model_name='budget',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='name',
            field=models.CharField(help_text='Name of the budget.', max_length=200),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='closet',
            field=models.ForeignKey(help_text='In what closet is the chemical.', on_delete=django.db.models.deletion.CASCADE, to='blog.Closet'),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='location',
            field=models.ForeignKey(help_text='Where it is the chemical.', on_delete=django.db.models.deletion.CASCADE, to='blog.Location'),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='unit_chemical',
            field=models.ForeignKey(help_text='Unit to the concentration/molecular weight of the chemical.', on_delete=django.db.models.deletion.CASCADE, to='blog.Unit_Chemical'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='chip',
            field=models.IntegerField(help_text='ID of the chip.'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='date',
            field=models.DateField(help_text='When was took.'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='laser_source',
            field=models.CharField(blank=True, help_text='Source of light that is used.', max_length=50),
        ),
        migrations.AlterField(
            model_name='chip',
            name='readout',
            field=models.CharField(blank=True, help_text='What type of sensor is used to read.', max_length=50),
        ),
        migrations.AlterField(
            model_name='chip',
            name='run',
            field=models.ForeignKey(help_text='To what run is assigned.', on_delete=django.db.models.deletion.CASCADE, to='blog.Run'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='user_name',
            field=models.ForeignKey(help_text='Who have the chip.', on_delete=django.db.models.deletion.CASCADE, to='blog.Full_Name_Users'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='wafer',
            field=models.ForeignKey(help_text='To what wafer is assigned.', on_delete=django.db.models.deletion.CASCADE, to='blog.Wafer'),
        ),
        migrations.AlterField(
            model_name='closet',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='closet',
            name='name',
            field=models.CharField(help_text='Name of the closet.', max_length=200),
        ),
        migrations.AlterField(
            model_name='computing',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='electronic',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='element',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='full_name_users',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='full_name_users',
            name='name',
            field=models.CharField(help_text='Full name of the users.', max_length=200),
        ),
        migrations.AlterField(
            model_name='instrumentation',
            name='characteristics',
            field=models.CharField(blank=True, help_text='Important features of the instrument.', max_length=200),
        ),
        migrations.AlterField(
            model_name='instrumentation',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='instrumentation',
            name='location',
            field=models.ForeignKey(help_text='Where it is the computer.', on_delete=django.db.models.deletion.CASCADE, to='blog.Location'),
        ),
        migrations.AlterField(
            model_name='instrumentation',
            name='manufacturer',
            field=models.CharField(blank=True, help_text='Manufacturer of the instrument.', max_length=200),
        ),
        migrations.AlterField(
            model_name='instrumentation',
            name='supplier',
            field=models.ForeignKey(help_text='Seller of the instrument.', on_delete=django.db.models.deletion.CASCADE, to='blog.Supplier'),
        ),
        migrations.AlterField(
            model_name='instrumentation',
            name='type_instrumentation',
            field=models.ForeignKey(help_text='Type of instrument to be stored.', on_delete=django.db.models.deletion.CASCADE, to='blog.Type_Instrumentation'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(help_text='Name of the location of the object.', max_length=200),
        ),
        migrations.AlterField(
            model_name='name_waveguide',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='name_waveguide',
            name='name',
            field=models.CharField(help_text='Name of the waveguide.', max_length=50),
        ),
        migrations.AlterField(
            model_name='number_closet',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='number_closet',
            name='name',
            field=models.CharField(help_text='Number of the closet.', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='applicant',
            field=models.CharField(help_text='Name of who do the order.', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.ForeignKey(help_text='Username of who create the order.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='budget',
            field=models.ForeignKey(help_text='Budget in where load the order.', on_delete=django.db.models.deletion.CASCADE, to='blog.Budget'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(help_text='Name of the order to save it.', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='number_product',
            field=models.IntegerField(default=1, help_text='Number of products to order.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_conditions',
            field=models.ForeignKey(help_text='Conditions of payment of the order.', on_delete=django.db.models.deletion.CASCADE, to='blog.Payment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(help_text='Who provide of components of the order.', on_delete=django.db.models.deletion.CASCADE, to='blog.Supplier'),
        ),
        migrations.AlterField(
            model_name='order',
            name='type_of_purchase',
            field=models.ForeignKey(help_text='Type of purchase of the order.', on_delete=django.db.models.deletion.CASCADE, to='blog.Type_of_purchase'),
        ),
        migrations.AlterField(
            model_name='others',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='others',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the component.', max_length=200),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(help_text='Name of the conditions of payment.', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(help_text='Description of the product.', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.ForeignKey(blank=True, help_text='To what order is assigned.', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(help_text='Quantity of the product that are ordered.', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.CharField(help_text='Price per unit of the product.', max_length=20),
        ),
        migrations.AlterField(
            model_name='run',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='run',
            name='run',
            field=models.IntegerField(help_text='ID of the run.'),
        ),
        migrations.AlterField(
            model_name='run',
            name='run_specifications',
            field=models.TextField(help_text='Specifications of the run.', max_length=500),
        ),
        migrations.AlterField(
            model_name='setup',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='setup',
            name='name',
            field=models.CharField(help_text='Name of the setup.', max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(help_text='Name of the supplier.', max_length=200),
        ),
        migrations.AlterField(
            model_name='type',
            name='author',
            field=models.ForeignKey(help_text='Name of the author that created the type.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='type',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(help_text='Name of the type of element.', max_length=200),
        ),
        migrations.AlterField(
            model_name='type_chemical',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='type_chemical',
            name='name',
            field=models.CharField(help_text='Name of the type of chemical.', max_length=200),
        ),
        migrations.AlterField(
            model_name='type_component',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='type_component',
            name='name',
            field=models.CharField(help_text='Name of the type of electronic component.', max_length=200),
        ),
        migrations.AlterField(
            model_name='type_instrumentation',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='type_instrumentation',
            name='name',
            field=models.CharField(help_text='Name of the type of instrument.', max_length=200),
        ),
        migrations.AlterField(
            model_name='type_object',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='type_object',
            name='name',
            field=models.CharField(help_text='Name of the part of the computer.', max_length=200),
        ),
        migrations.AlterField(
            model_name='type_of_purchase',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='type_of_purchase',
            name='name',
            field=models.CharField(help_text='Name of the purchase.', max_length=200),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(help_text='Unit of the electronic component.', max_length=200),
        ),
        migrations.AlterField(
            model_name='unit_chemical',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='unit_chemical',
            name='name',
            field=models.CharField(help_text='Unit of the chemical.', max_length=200),
        ),
        migrations.AlterField(
            model_name='wafer',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='wafer',
            name='run',
            field=models.ForeignKey(help_text='To what run is assigned.', on_delete=django.db.models.deletion.CASCADE, to='blog.Run'),
        ),
        migrations.AlterField(
            model_name='wafer',
            name='wafer',
            field=models.IntegerField(help_text='Id of the wafer.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='amplitude',
            field=models.FloatField(blank=True, help_text='Amplitude of the signal.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='chip',
            field=models.ForeignKey(help_text='To what chip is assigned.', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Chip'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date when was created.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='frecuency',
            field=models.FloatField(blank=True, help_text='Frequency of the signal.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='i_down',
            field=models.FloatField(blank=True, help_text=' Value of the current down.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='i_up',
            field=models.FloatField(blank=True, help_text='Value of the current up.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the waveguide.', max_length=100),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='noise',
            field=models.FloatField(blank=True, help_text='Noise in the signal.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='run',
            field=models.ForeignKey(help_text='To what run is assigned.', on_delete=django.db.models.deletion.CASCADE, to='blog.Run'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='slope',
            field=models.FloatField(blank=True, help_text='Slope of the signal.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='visibility',
            field=models.FloatField(blank=True, help_text='Visibility of th e signal.'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='wafer',
            field=models.ForeignKey(help_text='To what wafer is assigned.', on_delete=django.db.models.deletion.CASCADE, to='blog.Wafer'),
        ),
        migrations.AlterField(
            model_name='waveguide',
            name='waveguide',
            field=models.ForeignKey(blank=True, help_text='ID of the waveguide.', on_delete=django.db.models.deletion.CASCADE, to='blog.Name_Waveguide'),
        ),
        migrations.AddField(
            model_name='biological',
            name='closet',
            field=models.ForeignKey(help_text='In what closet is the biological component.', on_delete=django.db.models.deletion.CASCADE, to='blog.Closet'),
        ),
        migrations.AddField(
            model_name='biological',
            name='location',
            field=models.ForeignKey(help_text='Where it is the biological component.', on_delete=django.db.models.deletion.CASCADE, to='blog.Location'),
        ),
        migrations.AddField(
            model_name='biological',
            name='supplier',
            field=models.ForeignKey(help_text='Supplier of the biological component.', on_delete=django.db.models.deletion.CASCADE, to='blog.Supplier'),
        ),
        migrations.AddField(
            model_name='biological',
            name='type_biological',
            field=models.ForeignKey(help_text='Type of the biological component.', on_delete=django.db.models.deletion.CASCADE, to='blog.Type_Biological'),
        ),
        migrations.AddField(
            model_name='biological',
            name='unit_chemical',
            field=models.ForeignKey(help_text='Unit to the concentration/molecular weight of the chemical.', on_delete=django.db.models.deletion.CASCADE, to='blog.Unit_Chemical'),
        ),
    ]