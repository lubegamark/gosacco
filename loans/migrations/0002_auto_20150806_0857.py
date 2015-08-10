# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0002_auto_20150806_0811'),
        ('members', '__first__'),
        ('savings', '0002_auto_20150806_0811'),
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='securityshares',
            options={'verbose_name_plural': 'Security shares'},
        ),
        migrations.AddField(
            model_name='loan',
            name='application',
            field=models.ForeignKey(default=1, to='loans.LoanApplication'),
            preserve_default=False,
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
            field=models.ForeignKey(default=1, to='members.Member'),
            preserve_default=False,
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
            field=models.ForeignKey(default='shares', to='loans.LoanType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantors',
            field=models.ManyToManyField(related_name='backers', to='members.Member', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='member',
            field=models.ForeignKey(default=1, to='members.Member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='security',
            field=models.ManyToManyField(to='loans.Security', verbose_name=b'loan_security', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='type',
            field=models.ForeignKey(default='item', to='loans.LoanType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityarticle',
            name='owner',
            field=models.ForeignKey(default=1, to='members.Member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityarticle',
            name='security',
            field=models.ForeignKey(related_name='Item Security', default=1, to='loans.Security'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='guarantor',
            field=models.ForeignKey(default=1, to='members.Member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='savings_type',
            field=models.ForeignKey(default=1, to='savings.SavingsType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='security',
            field=models.ForeignKey(related_name='Savings Security', default=1, to='loans.Security'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityshares',
            name='share_type',
            field=models.ForeignKey(default=1, to='shares.ShareType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='security',
            name='attached_to_loan',
            field=models.ForeignKey(to='loans.LoanType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='security',
            name='security_type',
            field=models.CharField(max_length=50, choices=[(b'shares', b'shares'), (b'savings', b'savings'), (b'item', b'item')]),
            preserve_default=True,
        ),
    ]
