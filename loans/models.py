# Create your models here.
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.db.models import Model, FloatField, ForeignKey, DateField, BigIntegerField, IntegerField, ManyToManyField, \
    CharField, TextField, DateTimeField, OneToOneField
from django.utils.timezone import now

from polymorphic import PolymorphicModel

from members.models import Member
from savings.models import SavingsType, Savings
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
    name = CharField(max_length=50)
    interest = FloatField()
    interest_period = CharField(max_length=50, choices=INTEREST_PERIOD_CHOICES, default=YEAR)
    processing_period = IntegerField( help_text="In days")
    minimum_amount = BigIntegerField()
    maximum_amount = BigIntegerField()
    minimum_membership_period = IntegerField(help_text="In months(A month is 30 days)") #months
    minimum_share = IntegerField()
    minimum_savings = BigIntegerField()

    @classmethod
    def get_loan_types(cls):
        loan_types = cls.objects.filter()
        return loan_types

    def __unicode__(self):
        return self.name


class LoanRule(Model):

    ARTIFACT_CHOICES = (
         ('shares', 'shares'),
         ('savings', 'savings'),
     )
    artifact = CharField(max_length=100, choices=ARTIFACT_CHOICES)
    loan_type = ForeignKey(LoanType, related_name='extra_rules')
    share_type = ForeignKey(ShareType, blank=True, null=True)
    savings_type = ForeignKey(SavingsType, blank=True, null=True)
    minimum = BigIntegerField()
    maximum = BigIntegerField()


"""
class LoanTypeRequirements(Model):
    GREATER_THAN = 'gte'
    LESS_THAN = 'lte'
    EQUAL = 'equal'
    COMPARISON_CHOICES = (
        (GREATER_THAN, GREATER_THAN),
        (LESS_THAN, LESS_THAN),
        (EQUAL, EQUAL),
    )
    loan_type = ForeignKey(LoanType)
    rule_name = CharField(max_length=100)
    #rule_object =
    rule_comparison = CharField(max_length=50, choices=COMPARISON_CHOICES)
"""

# class Security(Model):
#     SHARES = 'shares'
#     SAVINGS = 'savings'
#     ITEM = 'item'
#     SECURITY_CHOICES = (
#         (SHARES, SHARES),
#         (SAVINGS, SAVINGS),
#         (ITEM, ITEM),
#     )
#     security_type = CharField(max_length=50,choices=SECURITY_CHOICES)
#     attached_to_loan = ForeignKey(LoanType)

#     def __unicode__(self):
#         return self.security_type  #self.get_security_model(self.security_type)


class Security(PolymorphicModel):
    member = ForeignKey(Member)

    attached_to_loan = IntegerField(blank=True, default=0, help_text="0 for none, or id of loan")

    @classmethod
    def get_members_securities(cls, member):
        loans = cls.objects.filter(member=member)
        return loans


class SecurityShares(Security):

    def share_value(self):
        return self.number_of_shares * self.share_type.share_price

    class Meta:
        verbose_name_plural ="Security shares"
    number_of_shares = IntegerField()
    share_type = ForeignKey(ShareType)
    value_of_shares = BigIntegerField(blank=True)

    def clean(self):
        available_shares = Shares.objects.get(share_type=self.share_type, member=self.member)
        if available_shares.number_of_shares < self.number_of_shares:
            raise ValidationError({"number_of_shares": "You don't have enough shares of class "+self.share_type.__str__()} )
        self.value_of_shares = self.share_value()

    def __unicode__(self):
        return str(self.number_of_shares)+" "+str(self.share_type)+" shares"


class SecuritySavings(Security):
    savings_type = ForeignKey(SavingsType)
    savings_amount = BigIntegerField()

    def clean(self):
        available_savings = Savings.objects.get(savings_type=self.savings_type, member=self.member)
        if available_savings.amount < self.savings_amount:
            raise ValidationError({"savings_amount": "You don't have enough savings of type "+self.savings_type.__str__()} )

    def __unicode__(self):
        return str(self.savings_amount)+" "+str(self.savings_type)+" savings"


class SecurityArticle(Security):
    name = CharField(max_length=100)
    type = CharField(max_length=100, help_text="eg Land, car, house")
    identification_type = CharField(max_length=100, help_text="eg Land title, car logbook")
    identification = CharField(max_length=100, help_text="eg ID Number, Title number")
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
    purpose = CharField(max_length=250, help_text="Purpose for the loan")
    payment_period = IntegerField(help_text="In Days eg. 90 days")
    loan_type = ForeignKey(LoanType, related_name="LoanType")
    status = CharField(max_length=25, choices=STATUS_CHOICES, default=PENDING, help_text="Current status of the application")
    security_details = TextField(help_text="Basic info provided about the security")
    security = ManyToManyField(Security, null=True, blank=True)
    #guarantors = ManyToManyField(Member, related_name=('backers'), blank=True)

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
    valid = False

    def meets_requirements(self):
        self.valid = True
        errors =[]
        if self.amount < self.loan_type.minimum_amount:
            self.valid = False
            error ='The minimum amount you can ask for is '+str(self.loan_type.minimum_amount)
            errors.append(error)
            print error

        if self.amount > self.loan_type.maximum_amount:
            self.valid = False
            error ='The maximum amount you can ask for is '+str(self.loan_type.maximum_amount)
            errors.append(error)
            print error

        membership_period = now().date() - self.member.registration_date
        if membership_period < timedelta(self.loan_type.minimum_membership_period*30):
            self.valid = False
            error ='You must be a member for at least '+str(self.loan_type.minimum_membership_period)+' months to be eligible'
            errors.append(error)
            print error

        return errors

    def clean(self):
        errors = self.meets_requirements()
        if self.valid is False:
            raise ValidationError(errors)

    def __unicode__(self):
        return self.member.user.username

    @classmethod
    def view_loan_applications(cls, member=None, ):
        pass

    def member_name(self):
        return ' '.join([self.member.user.first_name, self.member.user.last_name])



class Loan(Model):
    application = ForeignKey(LoanApplication)
    member = ForeignKey(Member)
    approval_date = DateTimeField()
    amount = BigIntegerField(help_text="Actual amount approved")
    payment_period = IntegerField(help_text="In days")
    loan_type = ForeignKey(LoanType)
    security_details = TextField(help_text="Basic info provided about the security")
    security = ManyToManyField(Security, blank=True, null=True)
    #guarantors = ManyToManyField(Member, related_name='Guarantors')

    @classmethod
    def get_members_loans(cls, member, loan_type=None):
        if loan_type is None:
            loans = cls.objects.filter(member=member)
        else:
            loans = cls.objects.filter(member=member, loan_type=loan_type)

        return loans


    def __unicode__(self):
        return self.member.user.username

