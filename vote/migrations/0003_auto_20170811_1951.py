# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20170808_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad_ent',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='ad_outdoor',
            name='img_url',
        ),
    ]