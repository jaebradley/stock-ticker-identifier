# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicly_traded_companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='company',
            unique_together=set([('exchange', 'ticker')]),
        ),
    ]