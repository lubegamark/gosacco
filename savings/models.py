from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField, BooleanField
from members.models import Member


class Saving(models.Model):
    member = ForeignKey(Member)
    amount = IntegerField()
    date = DateField()
    type = ForeignKey('SavingsType')

    def __unicode__(self):
        return self.member.user.username


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
    name = CharField(max_length=100)
    compulsory = BooleanField(default=True)
    interval = CharField(max_length=50, choices=INTERVAL_CHOICES, default=MONTH)
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()

    def __unicode__(self):
        return self.name