# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-05 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0094_update_preprintprovider_group_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectedguidmetadata',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='collectedguidmetadatas', to='osf.Subject'),
        ),
    ]
