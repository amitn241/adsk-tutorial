# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
        ('books', '0002_book_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_hard',
            field=models.ForeignKey(default=None, to='publishers.Publisher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_soft',
            field=models.ForeignKey(related_name='publisher_soft', blank=True, to='publishers.Publisher', null=True),
            preserve_default=True,
        ),
    ]
