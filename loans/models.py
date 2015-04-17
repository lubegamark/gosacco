# Create your models here.
from django.db.models import Model, FloatField, ForeignKey, DateField, BigIntegerField, IntegerField, ManyToManyField, \
    CharField, TextField

from members.models import Member


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
    minimum_membership_period = IntegerField()  # months
    minimum_share = IntegerField()
    minimum_savings = BigIntegerField()


    def __unicode__(self):
        return self.name


class SecurityArticle(Model):
    name = CharField(max_length=100)
    type = CharField(max_length=100)  # eg. (Land, car, house)
    identification_type = CharField(max_length=100)  #eg Land title, car logbook
    identification = CharField(max_length=100)
    attached_to_loan = IntegerField('Loan')
    owner = ForeignKey(Member)
    description = TextField()

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
    security = ForeignKey(SecurityArticle, null=True, blank=True)
    guarantors = ManyToManyField(Member, related_name='Proposed Guarantors')

    def __unicode__(self):
        return self.member.user.username


class Loan(Model):
    application = ForeignKey(LoanApplication)
    member = ForeignKey(Member)
    approval_date = DateField()
    amount = BigIntegerField()
    payment_period = IntegerField()
    type = ForeignKey(LoanType)
    security_details = TextField()
    security = ForeignKey(SecurityArticle, blank=True, null=True)
    guarantors = ManyToManyField(Member, related_name='Guarantors')

    def __unicode__(self):
        return self.member.user.username