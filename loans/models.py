# Create your models here.
from django.db.models import Model, FloatField, ForeignKey, DateField, BigIntegerField, IntegerField, ManyToManyField, \
    CharField, TextField
from polymorphic import PolymorphicModel
import members

from members.models import Member
from savings.models import SavingsType
from shares.models import Shares, ShareType


class LoanType(Model):
    YEAR = 'year'
    MONTH = 'month'
    DAY = 'day'
    INTEREST_PERIOD_CHOICES = (
        (YEAR, 'per anum'),
        (MONTH, 'per month'),
        (DAY, 'per day'),
    )
    name = CharField(max_length=255)
    interest = FloatField()
    interest_period = CharField(max_length=50, choices=INTEREST_PERIOD_CHOICES, default=YEAR)
    processing_period = IntegerField()
    minimum_amount = BigIntegerField()
    maximum_amount = BigIntegerField()
    minimum_membership_period = IntegerField() #months
    minimum_share = IntegerField()
    minimum_savings = BigIntegerField()

    @classmethod
    def get_loan_types(cls, member):
        loan_types = cls.objects.filter(member=member)
        return loan_types

    def __unicode__(self):
        return self.name


class Security(PolymorphicModel):
    SHARES = 'shares'
    SAVINGS = 'savings'
    ITEM = 'item'
    SECURITY_CHOICES = (
        (SHARES, SHARES),
        (SAVINGS, SAVINGS),
        (ITEM, ITEM),
    )
    #security_type = CharField(choices=SECURITY_CHOICES, max_length=50)
    #security_item =
    #member = ForeignKey(Member)
    attached_to_loan = IntegerField()

    @classmethod
    def get_members_securities(cls, member):
        loans = cls.objects.filter(member=member)
        return loans



class SecurityShares(Security):
    number_of_shares = IntegerField()
    share_type = ForeignKey(ShareType)
    value_of_shares = BigIntegerField()
    guarantor = ForeignKey(Member, related_name="Guarantor")
    member = ForeignKey(Member)
    #security = ForeignKey(Security, related_name='Shares Security')

    def __unicode__(self):
        return str(self.number_of_shares)+" "+str(self.share_type)+" shares"


class SecuritySavings(Security):
    savings_type = ForeignKey(SavingsType)
    savings_amount = BigIntegerField()
    member = ForeignKey(Member)
    #guarantor = ForeignKey(Member, related_name="Guarantor")
    #security = ForeignKey(Security, related_name='Savings Security')

    def __unicode__(self):
        return str(self.savings_amount)+" "+str(self.savings_type)+" savings"


class SecurityArticle(Security):
    name = CharField(max_length=100)
    type = CharField(max_length=100)  # eg. (Land, car, house)
    identification_type = CharField(max_length=100)  # eg Land title, car logbook
    identification = CharField(max_length=100)
    #attached_to_loan = IntegerField('Loan')
    #owner = ForeignKey(Member)
    member = ForeignKey(Member)
    description = TextField()
    #security = ForeignKey(Security, related_name='Item Security')

    def __unicode__(self):
        return self.name


class LoanApplication(Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )
    application_number = CharField(max_length=100)
    member = ForeignKey(Member)
    application_date = DateField()
    amount = BigIntegerField()
    payment_period = IntegerField(max_length=11)
    type = ForeignKey(LoanType)
    status = CharField(max_length=25, choices=STATUS_CHOICES, default=PENDING)
    security_details = TextField()
    security = ManyToManyField(Security, null=True, blank=True)
    guarantors = ManyToManyField(Member, related_name='Proposed Guarantors')

    def approve_loan_application(self):
        pass

    def reject_loan_application(self):
        pass

    def give_feedback_on_loan_application(self):
        pass

    @classmethod
    def get_members_loan_applications(cls, member, loan_type=None):
        if loan_type is None:
            loans = cls.objects.filter(member=member)
        else:
            loans = cls.objects.filter(member=member, loan_type=loan_type)

        return loans

    def __unicode__(self):
        return self.member.user.username

    @classmethod
    def view_loan_applications(cls, member=None, ):
        pass


class Loan(Model):
    application = ForeignKey(LoanApplication)
    member = ForeignKey(Member)
    approval_date = DateField()
    amount = BigIntegerField()
    payment_period = IntegerField()
    loan_type = ForeignKey(LoanType)
    security_details = TextField()
    security = ManyToManyField(Security, blank=True, null=True)
    guarantors = ManyToManyField(Member, related_name='Guarantors')

    @classmethod
    def get_members_loans(cls, member, loan_type=None):
        if loan_type is None:
            loans = cls.objects.filter(member=member)
        else:
            loans = cls.objects.filter(member=member, loan_type=loan_type)

        return loans

    def __unicode__(self):
        return self.member.user.username+" "