# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
        ('members', '__first__'),
        ('savings', '0001_initial'),
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
            name='Security',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('security_type', models.IntegerField(choices=[(b'shares', 1), (b'savings', 2), (b'item', 3)])),
                ('attached_to_loan', models.IntegerField()),
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
        migrations.CreateModel(
            name='SecuritySavings',
            fields=[
                ('security_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loans.Security')),
                ('savings_amount', models.BigIntegerField()),
                ('guarantor', models.ForeignKey(to='members.Member')),
                ('savings_type', models.ForeignKey(to='savings.SavingsType')),
            ],
            options={
            },
            bases=('loans.security',),
        ),
        migrations.CreateModel(
            name='SecurityShares',
            fields=[
                ('security_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loans.Security')),
                ('number_of_shares', models.IntegerField()),
                ('value_of_shares', models.BigIntegerField()),
                ('guarantor', models.ForeignKey(to='members.Member')),
                ('security', models.ForeignKey(related_name='Shares Security', to='loans.Security')),
                ('share_type', models.ForeignKey(to='shares.ShareType')),
            ],
            options={
            },
            bases=('loans.security',),
        ),
        migrations.AddField(
            model_name='securitysavings',
            name='security',
            field=models.ForeignKey(related_name='Savings Security', to='loans.Security'),
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
