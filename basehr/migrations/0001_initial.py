# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 18:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('blood_group', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(default='Karnataka', max_length=15)),
                ('pincode', models.IntegerField()),
                ('joining_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('marital_status', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=30)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('comment', models.TextField()),
                ('emp_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basehr.Department')),
            ],
        ),
        migrations.CreateModel(
            name='PastEmployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('past_employment_details', models.TextField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basehr.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='basehr.Employee'),
        ),
    ]
