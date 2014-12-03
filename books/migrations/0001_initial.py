# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('secondary_title', models.CharField(max_length=100, blank=True)),
                ('author', models.CharField(max_length=100)),
                ('copies', models.IntegerField(default=10)),
                ('published', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
