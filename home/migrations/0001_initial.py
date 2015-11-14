# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fist_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('credit_num', models.CharField(max_length=50)),
                ('cvv', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=50)),
                ('c_id', models.CharField(max_length=50)),
            ],
        ),
    ]
