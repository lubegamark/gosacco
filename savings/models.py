from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField, BooleanField
from django.utils import timezone
from django.utils.timezone import now
from members.models import Member, Group


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
            savings = cls.objects.filter(member=member)
        else:
            savings = cls.objects.filter(savings_type=current_savings_type, member=member)
        return savings
    
    @classmethod
    def get_savings(cls,  members=None, current_savings_type=None):
        if current_savings_type is None:
            if members is None:
                savings = cls.objects.all()
            elif isinstance(members, Member):
                savings = cls.objects.filter(member=members)
            elif isinstance(members, Group):
                #TODO Refactor these two statements inot one query
                group_members = Member.objects.filter(group__pk=members.pk)
                savings = cls.objects.filter(member__in=group_members)
            elif isinstance(members, list):
                savings = cls.objects.filter(member__in=members)
        elif isinstance(current_savings_type, SavingsType):
            if members is None:
                savings = cls.objects.filter(savings_type=current_savings_type)
            elif isinstance(members, Member):
                savings = cls.objects.filter(member=members, savings_type=current_savings_type)
            elif isinstance(members, Group):
                #TODO Refactor these two statements inot one query
                group_members = Member.objects.filter(group__pk=members.pk)
                savings = cls.objects.filter(member__in=group_members, savings_type=current_savings_type)
            elif isinstance(members, list):
                savings = cls.objects.filter(member__in=members, savings_type=current_savings_type)
        else:
            savings = []

        return savings


class SavingsWithdrawal(models.Model):
    amount = IntegerField()
    date = DateField()
    member = ForeignKey(Member)
    savings_type = ForeignKey(SavingsType)

    @classmethod
    def withdraw_savings(cls, member, savings_type, amount):

        try:
            savings = Savings.objects.get(member=member, savings_type=savings_type)
        except ObjectDoesNotExist:
            print member.user.username + " does not have any " + savings_type.name+" savings"
            return
        savings_withdrawal = cls(amount=amount, member=member, savings_type=savings_type, date=timezone.now())
        savings.amount -=amount
        savings_withdrawal.save()
        savings.save()

    @classmethod
    def get_withdrawals(cls, members=None, current_savings_type=None):
        if current_savings_type is None:
            if members is None:
                withdrawals = cls.objects.all()
            elif isinstance(members, Member):
                withdrawals = cls.objects.filter(member=members)
            elif isinstance(members, Group):
                #TODO Refactor these two statements inot one query
                group_members = Member.objects.filter(group__pk=members.pk)
                withdrawals = cls.objects.filter(member__in=group_members)
            elif isinstance(members, list):
                withdrawals = cls.objects.filter(member__in=members)
        elif isinstance(current_savings_type, SavingsType):
            if members is None:
                withdrawals = cls.objects.filter(savings_type=current_savings_type)
            elif isinstance(members, Member):
                withdrawals = cls.objects.filter(member=members, savings_type=current_savings_type)
            elif isinstance(members, Group):
                #TODO Refactor these two statements inot one query
                group_members = Member.objects.filter(group__pk=members.pk)
                withdrawals = cls.objects.filter(member__in=group_members, savings_type=current_savings_type)
            elif isinstance(members, list):
                withdrawals = cls.objects.filter(member__in=members, savings_type=current_savings_type)
        else:
            withdrawals = []

        return withdrawals


class SavingsPurchase(models.Model):
    amount = IntegerField()
    date = DateField()
    member = ForeignKey(Member)
    savings_type = ForeignKey(SavingsType)

    @classmethod
    def make_savings(cls, member, savings_type, amount, date=timezone.now()):
        try:
            savings = Savings.objects.get(member=member, savings_type=savings_type)
            savings.amount += amount

        except ObjectDoesNotExist:
            savings = Savings(member=member, savings_type=savings_type, amount=amount, date=date)

        finally:
            purchase = cls(member=member, savings_type=savings_type, amount=amount, date=date)
            purchase.save()
            savings.save()

    @classmethod
    def get_savings_purchases(cls, members=None, current_savings_type=None):
        if current_savings_type is None:
            if members is None:
                savings_purchases = cls.objects.all()
            elif isinstance(members, Member):
                savings_purchases = cls.objects.filter(member=members)
            elif isinstance(members, Group):
                #TODO Refactor these two statements inot one query
                group_members = Member.objects.filter(group__pk=members.pk)
                savings_purchases = cls.objects.filter(member__in=group_members)
            elif isinstance(members, list):
                savings_purchases = cls.objects.filter(member__in=members)
        elif isinstance(current_savings_type, SavingsType):
            if members is None:
                savings_purchases = cls.objects.filter(savings_type=current_savings_type)
            elif isinstance(members, Member):
                savings_purchases = cls.objects.filter(member=members, savings_type=current_savings_type)
            elif isinstance(members, Group):
                #TODO Refactor these two statements inot one query
                group_members = Member.objects.filter(group__pk=members.pk)
                savings_purchases = cls.objects.filter(member__in=group_members, savings_type=current_savings_type)
            elif isinstance(members, list):
                savings_purchases = cls.objects.filter(member__in=members, savings_type=current_savings_type)
        else:
            savings_purchases = []

        return savings_purchases
