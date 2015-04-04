# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20150331_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
    ]
