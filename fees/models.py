# Create your models here.
from django.db.models import Model, CharField, IntegerField, ForeignKey, DateTimeField
from members.models import Member


class Fee(Model):
    pass

class FeeType(Model):
    name = CharField(max_length=50)
    purpose = CharField(max_length=50)
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()

    def __unicode__(self):
        return self.name


class FeePayment(Model):
    member = ForeignKey(Member)
    fee_type = ForeignKey(FeeType)
    date = DateTimeField()
    amount = IntegerField()
    reason = CharField(max_length=250)

    def __unicode__(self):
        return str(self.member)
