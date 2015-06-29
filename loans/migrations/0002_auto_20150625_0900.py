# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0001_initial'),
        ('shares', '0001_initial'),
        ('loans', '0001_initial'),
        ('members', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='securityshares',
            name='share_type',
            field=models.ForeignKey(to='shares.ShareType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='guarantor',
            field=models.ForeignKey(to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='savings_type',
            field=models.ForeignKey(to='savings.SavingsType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='security',
            field=models.ForeignKey(related_name='Savings Security', to='loans.Security'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='securityarticle',
            name='owner',
            field=models.ForeignKey(to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='securityarticle',
            name='security',
            field=models.ForeignKey(related_name='Item Security', to='loans.Security'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantors',
            field=models.ManyToManyField(related_name='Proposed Guarantors', to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='member',
            field=models.ForeignKey(to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='security',
            field=models.ManyToManyField(to='loans.Security', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='type',
            field=models.ForeignKey(to='loans.LoanType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='application',
            field=models.ForeignKey(to='loans.LoanApplication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='guarantors',
            field=models.ManyToManyField(related_name='Guarantors', to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='member',
            field=models.ForeignKey(to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='security',
            field=models.ManyToManyField(to='loans.Security', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='type',
            field=models.ForeignKey(to='loans.LoanType'),
            preserve_default=True,
        ),
    ]
