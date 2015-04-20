# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boba_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
