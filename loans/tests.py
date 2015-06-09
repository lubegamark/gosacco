# Create your tests here.
from django.contrib.auth.models import User
from django.test.testcases import TestCase
from loans.models import LoanApplication, LoanType, Security, SecuritySavings
from members.models import Member
from savings.models import SavingsType


class LoansModelsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="fish", password="fhsdiauf")
        self.user2 = User.objects.create(username="bongo", password="fhsdiJFIDSNFud")
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
        self.security1 = Security.objects.create(
            security_type=Security.SECURITY_CHOICES[1][1],
            attached_to_loan=0,
        )

        self.loan_type1 = LoanType.objects.create(
            name="Short term",
            interest=0,
            interest_period=LoanType.YEAR,
            processing_period=5,
            minimum_amount=1000,
            maximum_amount=100000,
            minimum_membership_period=5,  # months
            minimum_share=12,
            minimum_savings=5,
        )

        self.savingType1 = SavingsType.objects.create(name="Annual",
                                                      compulsory=True,
                                                      interval=SavingsType.MONTH,
                                                      minimum_amount=20000,
                                                      maximum_amount=100000,
                                                      interest=1,
                                                      )

        self.savings_security1 = SecuritySavings.objects.create(
            savings_type=self.savingType1,
            savings_amount=50,
            guarantor=self.member2,
            security=self.security1,
        )


def test_get_security_model(self):
    self.assertEquals(self.security1.get_security_model(self.security1), 2)
