# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-07 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0012_auto_20160405_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='code_challenge',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='code_challenge_method',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
