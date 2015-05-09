# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharePurchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_share_price', models.IntegerField()),
                ('number_of_shares', models.IntegerField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_shares', models.IntegerField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShareTransfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_shares', models.IntegerField()),
                ('date', models.DateField()),
                ('giving_member', models.ForeignKey(related_name='Sender', to='members.Member')),
                ('receiving_member', models.ForeignKey(related_name='Recepient', to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShareType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_class', models.CharField(max_length=50)),
                ('share_price', models.BigIntegerField()),
                ('minimum_shares', models.BigIntegerField()),
                ('maximum_shares', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sharetransfer',
            name='share_type',
            field=models.ForeignKey(to='shares.ShareType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shares',
            name='share_type',
            field=models.ForeignKey(to='shares.ShareType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sharepurchase',
            name='share_type',
            field=models.ForeignKey(to='shares.ShareType'),
            preserve_default=True,
        ),
    ]