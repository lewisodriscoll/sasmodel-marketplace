# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0014_auto_20160906_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='sasviewmodel',
            name='in_library',
            field=models.BooleanField(default=False),
        ),
    ]
