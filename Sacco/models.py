from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import *


class Member(Model):
    user = OneToOneField(User)
    phone_number = CharField(max_length=50)
    registration_date = DateField()
    monthly_income = BigIntegerField()
    occupation = CharField(max_length=50)
    bank = CharField(max_length=50)
    account_number = IntegerField(max_length=50)
    signature = ImageField()
    id_number = CharField(max_length=50)
    id_type = CharField(max_length=50)
    address = CharField(max_length=250)
    city = CharField(max_length=250)
    nationality = CharField(max_length=250)
    comments = CharField(max_length=250)

    def __unicode__(self):
        return self.user.username


class Group(Model):
    name = CharField(max_length=50)
    location = CharField(max_length=100)
    address = CharField(max_length=100)
    leader = ForeignKey(Member, related_name='Group Leader')
    members = ManyToManyField(Member)

    def __unicode__(self):
        return self.name


class NextOfKin(Model):
    member = OneToOneField(Member)
    name = CharField(max_length=50)
    relationship = CharField(max_length=50)
    address = CharField(max_length=100)
    phone_number = CharField(max_length=50)
    occupation = CharField(max_length=50)
    comments = CharField(max_length=250)

    def __unicode__(self):
        return self.user.username

"""
class LoanType(Model):
    name = CharField(max_length=50)
    interest = FloatField()

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

    def __unicode__(self):
        return self.member.user.username


class SecurityArticle(Model):
    name = CharField(max_length=100)
    type = CharField(max_length=50)
    identification = CharField(max_length=100)
    loan_application = ForeignKey(LoanApplication)

    def __unicode__(self):
        return self.name


class Guarantor(Model):
    name = CharField(max_length=50)
    address = CharField(max_length=100)
    phone_number = CharField(max_length=50)
    occupation = CharField(max_length=50)
    loan_application = ForeignKey(LoanApplication)

    def __unicode__(self):
        return self.name
"""