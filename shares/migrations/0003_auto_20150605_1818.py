# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0002_auto_20150513_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharetransfer',
            old_name='receiving_member',
            new_name='buyer',
        ),
        migrations.RenameField(
            model_name='sharetransfer',
            old_name='giving_member',
            new_name='seller',
        ),
    ]
