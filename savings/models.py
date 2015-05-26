from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField, BooleanField
from django.utils import timezone
from members.models import Member


class SavingsType(models.Model):
    YEAR = 'year'
    MONTH = 'month'
    WEEK = 'week'
    DAY = 'day'
    INTERVAL_CHOICES = (
        (YEAR, 'per anum'),
        (MONTH, 'per month'),
        (WEEK, 'per week'),
        (DAY, 'per day'),
    )

    FIXED = 'fixed'
    CONTRACT = 'contract'
    CURRENT = 'current'
    TARGET = 'target'

    CATEGORY_CHOICES = (
        (FIXED, 'fixed'),
        (CONTRACT, 'contract'),
        (CURRENT, 'current'),
        (TARGET, 'target'),
    )
    name = CharField(max_length=100)
    category = CharField(max_length=50, choices=CATEGORY_CHOICES, default=FIXED)
    compulsory = BooleanField(default=True)
    interval = CharField(max_length=50, choices=INTERVAL_CHOICES, default=MONTH)
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()
    interest = IntegerField()

    def __unicode__(self):
        return self.name


class Savings(models.Model):
    member = ForeignKey(Member)
    amount = IntegerField()
    date = DateField()
    savings_type = ForeignKey(SavingsType)

    def __unicode__(self):
        return self.member.user.username

    @classmethod
    def get_members_savings(cls, member, current_savings_type=None):
        if current_savings_type is None:
            savings = Savings.objects.filter(member=member)
        else:
            savings = Savings.objects.filter(savings_type=current_savings_type, member=member)
        return savings

    @classmethod
    def withdraw_savings(cls, member, savings_type, amount):

        try:
            savings = Savings.objects.get(member=member, savings_type=savings_type)
        except ObjectDoesNotExist:
            print member.user.username + " does not have any " + savings_type.name+" savings"
            return
        savings_withdrawal = SavingsWithdrawal(amount=amount, member=member, savings_type=savings_type, date=timezone.now())
        savings_withdrawal.save()
        savings.save()


class SavingsWithdrawal(models.Model):
    amount = IntegerField()
    date = DateField()
    member = ForeignKey(Member)
    savings_type = ForeignKey(SavingsType)


class SavingsPurchase(models.Model):
    amount = IntegerField()
    date = DateField()
    member = ForeignKey(Member)
    savings_type = ForeignKey(SavingsType)

    @classmethod
    def make_savings(cls, member, savings_type, amount, date):
        try:
            savings = Savings.objects.get(member=member, savings_type=savings_type)
            savings.amount += amount

        except ObjectDoesNotExist:
            savings = Savings(member=member, savings_type=savings_type, amount=amount, date=date)

        finally:
            purchase = SavingsPurchase(member=member, savings_type=savings_type, amount=amount, date=date)
            purchase.save()
            savings.save()