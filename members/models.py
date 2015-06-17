from django.contrib.auth.models import User
from django.db.models import *


class Member(Model):
    user = OneToOneField(User)
    phone_number = CharField(max_length=50)
    registration_date = DateField()
    monthly_income = BigIntegerField()
    occupation = CharField(max_length=250)
    bank = CharField(max_length=250)
    account_number = CharField(max_length=250)
    signature = ImageField()
    id_type = CharField(max_length=250)
    id_number = CharField(max_length=250)
    address = CharField(max_length=250)
    city = CharField(max_length=250)
    nationality = CharField(max_length=250)
    comments = TextField()

    def __unicode__(self):
        return self.user.username


class Group(Model):
    name = CharField(max_length=100)
    location = CharField(max_length=100)
    address = CharField(max_length=250)
    leader = ForeignKey(Member, related_name='Group Leader')
    members = ManyToManyField(Member)

    def __unicode__(self):
        return self.name


class NextOfKin(Model):
    member = OneToOneField(Member)
    name = CharField(max_length=100)
    relationship = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    occupation = CharField(max_length=50)
    comments = CharField(max_length=250)
    address = CharField(max_length=250)
    current_village = CharField(max_length=100)
    current_subcounty = CharField(max_length=100)
    current_district = CharField(max_length=100)
    permanent_village = CharField(max_length=100)
    pernament_subcounty = CharField(max_length=100)
    permanent_district = CharField(max_length=100)
    signature = ImageField()

    def __unicode__(self):
        return self.member.user.username
