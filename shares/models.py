from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField, ManyToManyField
from members.models import Member


class Share(models.Model):
    member = ManyToManyField(Member)
    amount = IntegerField()
    date = DateField()
    type = ForeignKey('ShareType')


class ShareType(models.Model):
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
    share_class = CharField()
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()