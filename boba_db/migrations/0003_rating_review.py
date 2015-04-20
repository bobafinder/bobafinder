# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boba_db', '0002_auto_20150416_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.ForeignKey(blank=True, null=True, to='boba_db.Review'),
        ),
    ]
