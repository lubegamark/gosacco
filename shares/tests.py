# Create your tests here.
import os
from django.contrib.auth.models import User
from django.test import TestCase
from members.models import Member

from shares.models import Shares, ShareType, SharePurchase, ShareTransfer


class SharesModelsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="fish", password="fhsdiauf")
        self.user2 = User.objects.create(username="bongo", password="fhsdiJFIDSNFud")
        self.shareType1 = ShareType.objects.create(share_class="A",
                                                   share_price=10000,
                                                   minimum_shares=0,
                                                   maximum_shares=5000,
                                                   )
        self.shareType2 = ShareType.objects.create(share_class="B",
                                                   share_price=12000,
                                                   minimum_shares=10,
                                                   maximum_shares=500,
                                                   )
        self.member1 = Member.objects.create(user=self.user1,
                                             phone_number="445465",
                                             registration_date="2015-12-15",
                                             monthly_income="448824",
                                             occupation="Fish",
                                             bank="DFCU",
                                             account_number="78514",
                                             signature="",
                                             id_type="Driving Permit",
                                             id_number="7654",
                                             address="Wano",
                                             city="KLA",
                                             nationality="Ug",
                                             comments="Bongo",
                                             )
        self.member2 = Member.objects.create(user=self.user2,
                                             phone_number="445465",
                                             registration_date="2015-12-15",
                                             monthly_income="448824",
                                             occupation="Fish",
                                             bank="Centenary",
                                             account_number="78s514",
                                             signature="",
                                             id_type="National ID",
                                             id_number="7654354654",
                                             address="Wano si wa ",
                                             city="Wakiso",
                                             nationality="Ug",
                                             comments="Bongo huh",
                                             )
        self.share1 = Shares.objects.create(member=self.member1,
                                            number_of_shares=5,
                                            date="2014-12-12",
                                            share_type=self.shareType1,
                                            )
        self.share2 = Shares.objects.create(member=self.member1,
                                            number_of_shares=4,
                                            date="2014-01-12",
                                            share_type=self.shareType2,
                                            )
        self.share3 = Shares.objects.create(member=self.member2,
                                            number_of_shares=4,
                                            date="2014-01-12",
                                            share_type=self.shareType1,
                                            )

    def test_get_members_shares(self):
        shares = Shares.get_members_shares(self.member1)
        self.assertSequenceEqual(shares, [self.share1, self.share2])

    def test_get_members_shares_with_sharetype(self):
        shares = Shares.get_members_shares(self.member1, self.shareType1)
        self.assertSequenceEqual(shares, [self.share1])

    def test_issue_shares(self):
        shares = 10
        all_shares_before_purchase = Shares.get_members_shares(self.member1, self.shareType1)
        shares_before_purchase = all_shares_before_purchase[0]
        SharePurchase.issue_shares(self.member1, shares, self.shareType1)
        all_shares_after_purchase = Shares.get_members_shares(self.member1, self.shareType1)
        shares_after_purchase = all_shares_after_purchase[0]
        all_purchases = SharePurchase.objects.all()
        purchase = all_purchases[0]
        self.assertEquals(shares, purchase.number_of_shares)
        self.assertEquals(shares_after_purchase.number_of_shares,
                          purchase.number_of_shares + shares_before_purchase.number_of_shares)

    def test_transfer_shares(self):
        new_shares = 3
        sellers_shares_before = Shares.get_members_shares(self.member1, self.shareType1)[0]
        buyers_shares_before = Shares.get_members_shares(self.member2, self.shareType1)[0]

        ShareTransfer.transfer_shares(self.member1, self.member2, new_shares, self.shareType1)

        sellers_shares_after = Shares.get_members_shares(self.member1, self.shareType1)[0]
        buyers_shares_after = Shares.get_members_shares(self.member2, self.shareType1)[0]

        self.assertEquals(sellers_shares_after.number_of_shares, sellers_shares_before.number_of_shares - new_shares)
        self.assertEquals(buyers_shares_after.number_of_shares, buyers_shares_before.number_of_shares + new_shares)

    def test_transfer_shares_excess(self):
        new_shares = 10
        sellers_shares_before = Shares.get_members_shares(self.member1, self.shareType1)[0]
        buyers_shares_before = Shares.get_members_shares(self.member2, self.shareType1)[0]

        ShareTransfer.transfer_shares(self.member1, self.member2, new_shares, self.shareType1)

        sellers_shares_after = Shares.get_members_shares(self.member1, self.shareType1)[0]
        buyers_shares_after = Shares.get_members_shares(self.member2, self.shareType1)[0]

        self.assertEquals(sellers_shares_after.number_of_shares, sellers_shares_before.number_of_shares)
        self.assertEquals(buyers_shares_after.number_of_shares, buyers_shares_before.number_of_shares)

    def test_transfer_shares_seller_without_shares(self):
        new_shares = 2
        share_transfers_before = ShareTransfer.objects.all()

        ShareTransfer.transfer_shares(self.member2, self.member1, new_shares, self.shareType2)
        share_transfers_after = ShareTransfer.objects.all()

        self.assertSequenceEqual(Shares.get_members_shares(self.member2, self.shareType2), [])
        # self.assertSequenceEqual(share_transfers_before, share_transfers_after)