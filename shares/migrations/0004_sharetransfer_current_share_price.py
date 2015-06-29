# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0003_auto_20150605_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharetransfer',
            name='current_share_price',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
