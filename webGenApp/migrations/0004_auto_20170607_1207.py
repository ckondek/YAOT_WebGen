# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webGenApp', '0003_auto_20170604_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='picChoice',
            field=models.CharField(choices=[('base1.jpg', 'pic1'), ('base2.jpg', 'pic2'), ('base3.jpg', 'pic3')], default='base2.jpg', max_length=12),
        ),
        migrations.AlterField(
            model_name='person',
            name='show',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webGenApp.Show'),
        ),
    ]