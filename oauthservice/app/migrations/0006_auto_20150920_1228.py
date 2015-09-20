# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150920_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='token',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
