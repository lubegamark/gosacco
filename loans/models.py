# Create your models here.
from django.db.models import Model, FloatField, ForeignKey, DateField, BigIntegerField, IntegerField, ManyToManyField, \
    CharField, TextField

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

    def __unicode__(self):
        return self.name


class Security(Model):
    SHARES = 'shares'
    SAVINGS = 'savings'
    ITEM = 'item'
    SECURITY_CHOICES = (
        (SHARES, SHARES),
        (SAVINGS, SAVINGS),
        (ITEM, ITEM),
    )
    security_type = CharField(max_length=50,choices=SECURITY_CHOICES)
    attached_to_loan = ForeignKey(LoanType)

    def __unicode__(self):
        return self.security_type  #self.get_security_model(self.security_type)

    def get_security_model(self, security_type):
        if security_type is self.SHARES:
            security_model = SecurityShares
        elif security_type is self.SAVINGS:
            security_model = SecuritySavings
        else:
            security_model = SecurityArticle

        return security_model


class SecurityShares(Security):
    class Meta:
        verbose_name_plural ="Security shares"
    number_of_shares = IntegerField()
    share_type = ForeignKey(ShareType)
    value_of_shares = BigIntegerField()
    guarantor = ForeignKey(Member)
    security = ForeignKey(Security, related_name='Shares Security')

    def __unicode__(self):
        return 'Shares'


class SecuritySavings(Security):
    savings_type = ForeignKey(SavingsType)
    savings_amount = BigIntegerField()
    guarantor = ForeignKey(Member)
    security = ForeignKey(Security, related_name='Savings Security')

    def __unicode__(self):
        return 'Savings'


class SecurityArticle(Model):
    name = CharField(max_length=100)
    type = CharField(max_length=100)  # eg. (Land, car, house)
    identification_type = CharField(max_length=100)  #eg Land title, car logbook
    identification = CharField(max_length=100)
    attached_to_loan = IntegerField('Loan')
    owner = ForeignKey(Member)
    description = TextField()
    security = ForeignKey(Security, related_name='Item Security')

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
    security = ManyToManyField(Security, verbose_name=('loan_security'), blank=True)
    guarantors = ManyToManyField(Member, related_name=('backers'), blank=True)

    def __unicode__(self):
        return self.member.user.username

    def member_name(self):
        return ' '.join([self.member.user.first_name, self.member.user.last_name])


class Loan(Model):
    application = ForeignKey(LoanApplication)
    member = ForeignKey(Member)
    approval_date = DateField()
    amount = BigIntegerField()
    payment_period = IntegerField()
    type = ForeignKey(LoanType)
    security_details = TextField()
    security = ManyToManyField(Security, blank=True, null=True)
    guarantors = ManyToManyField(Member, related_name='Guarantors')

    def __unicode__(self):
        return self.member.user.username
