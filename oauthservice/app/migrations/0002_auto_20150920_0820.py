# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=40)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AccessToken',
        ),
        migrations.DeleteModel(
            name='Grant',
        ),
        migrations.DeleteModel(
            name='RefreshToken',
        ),
        migrations.RemoveField(
            model_name='client',
            name='grant_type',
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
