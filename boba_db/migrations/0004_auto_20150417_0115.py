# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boba_db', '0003_rating_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='value',
            new_name='score',
        ),
    ]
