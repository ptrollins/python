# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_student',
            field=models.PositiveSmallIntegerField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='exercise',
            unique_together=set([('id_app', 'id_exercise')]),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('student', 'date')]),
        ),
    ]
