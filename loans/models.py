# Create your models here.
from django.db.models import Model, FloatField, ForeignKey, DateField, BigIntegerField, IntegerField, ManyToManyField, \
    CharField

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
    name = CharField(max_length=50)
    interest = FloatField(max_length=50)
    interest_period = CharField(max_length=50, choices=INTEREST_PERIOD_CHOICES, default=YEAR)
    processing_period = IntegerField()
    minimum_amount = IntegerField()
    maximum_amount = IntegerField()
    minimum_membership_period = IntegerField()
    minimum_share = IntegerField()
    minimum_savings = IntegerField()


    def __unicode__(self):
        return self.name


class SecurityArticle(Model):
    name = CharField(max_length=100)
    type = CharField(max_length=50)  # eg. (Land, car, house)
    identification_type = CharField(max_length=100)  #eg Land title, car logbook
    identification = CharField(max_length=100)
    attached_to_loan = IntegerField('Loan', null=True)
    owner = ForeignKey(Member)
    description = CharField(max_length=250)

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
    status = CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    security_details = CharField(max_length=50)
    security = ForeignKey(SecurityArticle)
    guarantors = ManyToManyField(Member, related_name='Proposed Guarantors')

    def __unicode__(self):
        return self.member.user.username


class Loan(Model):
    application = ForeignKey(LoanApplication)
    member = ForeignKey(Member)
    approval_date = DateField()
    amount = BigIntegerField()
    payment_period = IntegerField(max_length=11)
    type = ForeignKey(LoanType)
    security_details = CharField(max_length=50)
    security = ForeignKey(SecurityArticle, blank=True, null=True)
    guarantors = ManyToManyField(Member, related_name='Guarantors')
