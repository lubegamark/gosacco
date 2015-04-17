from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField
from members.models import Member


class Share(models.Model):
    member = ForeignKey(Member)
    amount = IntegerField()
    number_of_shares = IntegerField()
    date = DateField()
    type = ForeignKey('ShareType')

    def __unicode__(self):
        return self.member.user.username


class ShareType(models.Model):
    share_class = CharField(max_length=50)
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()

    def __unicode__(self):
        return self.share_class