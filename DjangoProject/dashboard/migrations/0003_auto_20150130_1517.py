# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150130_0610'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('student', 'date', 'exercise')]),
        ),
    ]
