# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False, max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('following', models.ManyToManyField(to='social.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.CharField(max_length=4096)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.OneToOneField(to='social.Profile', null=True),
            preserve_default=True,
        ),
    ]
