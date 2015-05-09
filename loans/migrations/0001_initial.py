# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approval_date', models.DateField()),
                ('amount', models.BigIntegerField()),
                ('payment_period', models.IntegerField()),
                ('security_details', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_number', models.CharField(max_length=100)),
                ('application_date', models.DateField()),
                ('amount', models.BigIntegerField()),
                ('payment_period', models.IntegerField(max_length=11)),
                ('status', models.CharField(default=b'pending', max_length=25, choices=[(b'pending', b'Pending'), (b'approved', b'Approved'), (b'rejected', b'Rejected')])),
                ('security_details', models.TextField()),
                ('guarantors', models.ManyToManyField(related_name='Proposed Guarantors', to='members.Member')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('interest', models.FloatField()),
                ('interest_period', models.CharField(default=b'year', max_length=50, choices=[(b'year', b'per anum'), (b'month', b'per month'), (b'day', b'per day')])),
                ('processing_period', models.IntegerField()),
                ('minimum_amount', models.BigIntegerField()),
                ('maximum_amount', models.BigIntegerField()),
                ('minimum_membership_period', models.IntegerField()),
                ('minimum_share', models.IntegerField()),
                ('minimum_savings', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecurityArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('identification_type', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('attached_to_loan', models.IntegerField(verbose_name=b'Loan')),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='security',
            field=models.ForeignKey(blank=True, to='loans.SecurityArticle', null=True),
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
            field=models.ForeignKey(blank=True, to='loans.SecurityArticle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='type',
            field=models.ForeignKey(to='loans.LoanType'),
            preserve_default=True,
        ),
    ]
