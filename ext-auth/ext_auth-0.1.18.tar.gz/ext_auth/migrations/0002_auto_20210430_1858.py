# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ext_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='externaluseridentifier',
            options={'verbose_name': 'External User', 'verbose_name_plural': 'External Users'},
        ),
    ]
