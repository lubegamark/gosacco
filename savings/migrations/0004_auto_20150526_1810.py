# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0003_savingspurchase_savingswithdrawal'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingstype',
            name='category',
            field=models.CharField(default=b'fixed', max_length=50, choices=[(b'fixed', b'fixed'), (b'contract', b'contract'), (b'current', b'current'), (b'target', b'target')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='savingstype',
            name='interest',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
