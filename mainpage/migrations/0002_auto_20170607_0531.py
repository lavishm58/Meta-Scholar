# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mainpage',
            new_name='social_auth_usersocialauth',
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobilephone',
            field=models.IntegerField(),
        ),
    ]