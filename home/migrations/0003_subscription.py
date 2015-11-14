# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151114_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_nonce', models.CharField(max_length=100, null=True, blank=True)),
                ('amount', models.CharField(max_length=100, null=True, blank=True)),
                ('txnid', models.CharField(max_length=25, null=True, blank=True)),
                ('result', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(related_name='subscription', to='home.Staff')),
            ],
        ),
    ]
