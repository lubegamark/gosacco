# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='attached_to_loan',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
