from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from savings.models import Savings, SavingsType, SavingsPurchase, SavingsWithdrawal
from django.contrib.auth.models import User
from members.models import Member, Group, NextOfKin



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        depth = 0

class SavingsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsType
        fields = ('id','name','category','compulsory','interval','minimum_amount','maximum_amount','interest')


class SavingsSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    savings_type = SavingsTypeSerializer()
    class Meta:
        model = Savings
        fields = ('id','member','amount','date','savings_type')

class CreateSavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = ('id','member','amount','date','savings_type')


class SavingsPurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = SavingsPurchase
		fields = ('id','amount','date','member','savings_type')

class SavingsWithdrawSerializer(serializers.ModelSerializer):
	class Meta:
		model = SavingsWithdrawal
		fields = ('id','amount','date','member','savings_type')
