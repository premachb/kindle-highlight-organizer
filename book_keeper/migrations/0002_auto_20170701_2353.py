# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_keeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_length',
            field=models.IntegerField(null=True),
        ),
    ]
