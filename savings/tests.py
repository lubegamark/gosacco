# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from members.models import Member
from savings.models import SavingsType, Savings, SavingsPurchase


class SavingsModelsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="fish", password="fhsdiauf")
        self.user2 = User.objects.create(username="bongo", password="fhsdiJFIDSNFud")
        self.savingType1 = SavingsType.objects.create(name="Annual",
                                                      compulsory=True,
                                                      interval=SavingsType.MONTH,
                                                      minimum_amount=20000,
                                                      maximum_amount=100000,
                                                      )
        self.savingType2 = SavingsType.objects.create(name="New Office",
                                                      compulsory=False,
                                                      interval=SavingsType.MONTH,
                                                      minimum_amount=1000,
                                                      maximum_amount=0,
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
        self.saving1 = Savings.objects.create(member=self.member1,
                                             amount=50000,
                                             date="2014-12-12",
                                             savings_type=self.savingType1,
                                             )
        self.saving2 = Savings.objects.create(member=self.member1,
                                             amount=2500,
                                             date="2014-01-12",
                                             savings_type=self.savingType2,
                                             )
        self.saving3 = Savings.objects.create(member=self.member2,
                                             amount=20000,
                                             date="2014-01-12",
                                             savings_type=self.savingType1,
                                             )


    def test_get_members_savings(self):
        savings = Savings.get_members_savings(self.member1)
        self.assertSequenceEqual(savings, [self.saving1, self.saving2])

    def test_get_members_savings_with_savingstype(self):
        savings = Savings.get_members_savings(self.member1, self.savingType1)
        self.assertSequenceEqual(savings, [self.saving1])

    def test_make_savings(self):
        new_savings = 5000
        savings_before = Savings.objects.get(member=self.member1, savings_type=self.savingType1)
        self.assertEqual(savings_before, self.saving1)
        SavingsPurchase.make_savings(self.member1, self.savingType1, new_savings, timezone.now())
        savings_after = Savings.objects.get(member=self.member1, savings_type=self.savingType1)
        self.assertEqual(savings_after, self.saving1)
        self.assertEqual(savings_before.amount+new_savings, savings_after.amount)
