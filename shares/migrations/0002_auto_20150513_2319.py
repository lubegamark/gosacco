# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shares',
            unique_together=set([('member', 'share_type')]),
        ),
    ]
