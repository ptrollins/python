# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_app', models.PositiveSmallIntegerField()),
                ('id_exercise', models.PositiveSmallIntegerField()),
                ('scoremax_possible', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('score', models.PositiveSmallIntegerField()),
                ('exercise', models.ForeignKey(to='dashboard.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_student', models.PositiveSmallIntegerField()),
                ('id_school', models.PositiveSmallIntegerField()),
                ('id_class', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['id_student'],
                'verbose_name_plural': 'oxen',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(to='dashboard.Student'),
            preserve_default=True,
        ),
    ]
