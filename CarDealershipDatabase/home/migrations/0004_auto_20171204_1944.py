# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-05 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171204_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]