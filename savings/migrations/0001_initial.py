# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SavingsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('compulsory', models.BooleanField(default=True)),
                ('interval', models.CharField(default=b'month', max_length=50, choices=[(b'year', b'per anum'), (b'month', b'per month'), (b'week', b'per week'), (b'day', b'per day')])),
                ('minimum_amount', models.IntegerField()),
                ('maximum_amount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='saving',
            name='type',
            field=models.ForeignKey(to='savings.SavingsType'),
            preserve_default=True,
        ),
    ]
