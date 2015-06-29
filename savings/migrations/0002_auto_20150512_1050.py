# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '__first__'),
        ('savings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(to='members.Member')),
                ('savings_type', models.ForeignKey(to='savings.SavingsType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='saving',
            name='member',
        ),
        migrations.RemoveField(
            model_name='saving',
            name='type',
        ),
        migrations.DeleteModel(
            name='Saving',
        ),
    ]
