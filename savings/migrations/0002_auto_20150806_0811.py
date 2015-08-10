# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='savings',
            options={'verbose_name_plural': 'Savings'},
        ),
        migrations.AlterModelOptions(
            name='savingspurchase',
            options={'verbose_name_plural': 'Savings Purchase'},
        ),
        migrations.AlterModelOptions(
            name='savingswithdrawal',
            options={'verbose_name_plural': 'Savings Withdraw'},
        ),
    ]
