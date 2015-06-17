# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nextofkin',
            old_name='pernament_subcounty',
            new_name='permanent_subcounty',
        ),
    ]
