# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('primary_key', models.IntegerField(primary_key=None)),
                ('auth', models.CharField(max_length=16)),
                ('recip', models.CharField(max_length=16)),
                ('pm', models.BooleanField(default=False)),
                ('time', models.DateTimeField()),
                ('message', models.CharField(max_length=4096)),
                ('user', models.ForeignKey(to='social.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
