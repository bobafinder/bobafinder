# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('caption', models.TextField()),
                ('date_added', models.DateField()),
                ('date_updated', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.IntegerField()),
                ('headline', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('date_added', models.DateField()),
                ('date_updated', models.DateField()),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('date_added', models.DateField()),
                ('date_updated', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='store',
            field=models.ForeignKey(to='boba_db.Store'),
        ),
    ]
