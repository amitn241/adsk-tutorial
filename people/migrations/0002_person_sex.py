# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Male'), (2, b'Female')]),
            preserve_default=False,
        ),
    ]
