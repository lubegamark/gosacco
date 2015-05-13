from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, IntegerField, DateField, CharField, BigIntegerField
from django.utils import timezone
from django.utils.datetime_safe import date
from members.models import Member


class ShareType(models.Model):
    share_class = CharField(max_length=50)
    share_price = BigIntegerField()
    minimum_shares = BigIntegerField()
    maximum_shares = BigIntegerField()

    def __unicode__(self):
        return self.share_class


class Shares(models.Model):
    member = ForeignKey(Member)
    share_type = ForeignKey(ShareType)
    number_of_shares = IntegerField()
    date = DateField()

    class Meta:
        unique_together = ("member", "share_type")

    def __unicode__(self):
        return self.member.user.username

    """
    Get a members shares
    """
    @classmethod
    def get_members_shares(cls, member, current_share_type=None):
        if current_share_type is None:
            shares = Shares.objects.filter(member=member)
        else:
            shares = Shares.objects.filter(share_type=current_share_type, member=member)
        return shares


class SharePurchase(models.Model):
    member = ForeignKey(Member)
    current_share_price = IntegerField()
    number_of_shares = IntegerField()
    date = DateField()
    share_type = ForeignKey(ShareType)

    """
    Issue new stock to member
    """
    @classmethod
    def issue_shares(cls, member, shares, share_type):
        try:
            share_price = share_type.share_price
            purchase = SharePurchase(member=member, number_of_shares=shares, current_share_price=share_price,
                                     share_type=share_type, date=timezone.now())
            purchase.save()
            member_shares = Shares.objects.get(member=member, share_type=share_type)
            member_shares.number_of_shares += shares
            member_shares.save()
        except:
            return False

        return True


class ShareTransfer(models.Model):
    giving_member = ForeignKey(Member, related_name="Sender")
    receiving_member = ForeignKey(Member, related_name="Recepient")
    # amount = IntegerField()
    number_of_shares = IntegerField()
    date = DateField()
    share_type = ForeignKey(ShareType)

    def __unicode__(self):
        return str(self.number_of_shares)+" "+"class "+self.share_type.share_class+" shares from "+self.giving_member.user.username+" to "+self.receiving_member.user.username

    """
    Transfer shares from one member to another

    """
    @classmethod
    def transfer_shares(cls, seller, buyer, number_of_shares, share_type):
        try:
            seller_shares = Shares.objects.get(member=seller, share_type=share_type)
        except ObjectDoesNotExist as e:
            print "The seller does not posses shares of that type"
            return

        try:
            buyer_shares = Shares.objects.get(member=buyer, share_type=share_type)
        except ObjectDoesNotExist:
            buyer_shares = Shares(member=buyer, share_type=share_type, number_of_shares=0, date=timezone.now())
            buyer_shares.save()

        if seller_shares.number_of_shares < number_of_shares:
            print "You do not have enough shares"
            return
        else:
            transfer = ShareTransfer(giving_member=seller, receiving_member=buyer, number_of_shares=number_of_shares,
                                     share_type=share_type, date=timezone.now())

            buyer_shares.number_of_shares += number_of_shares
            seller_shares.number_of_shares -= number_of_shares

            transfer.save()
            buyer_shares.save()
            seller_shares.save()