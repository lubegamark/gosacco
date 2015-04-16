from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField, BooleanField, ManyToManyField
from members.models import Member


class Saving(models.Model):
    member = ManyToManyField(Member)
    amount = IntegerField()
    date = DateField()
    type = ForeignKey('SavingsType')


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
    name = CharField()
    compulsory = BooleanField(default=True)
    interval = CharField(max_length=50, choices=INTERVAL_CHOICES, default=MONTH)
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()