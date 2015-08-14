from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from members.serializers import MemberSerializer, MemberUserSerializer

from savings.models import Savings, SavingsType, SavingsDeposit, SavingsWithdrawal
from django.contrib.auth.models import User
from members.models import Member, Group, NextOfKin



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


class SavingsDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsDeposit
        fields = ('id','amount','date','member','savings_type')

class SavingsWithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsWithdrawal
        fields = ('id','amount','date','member','savings_type')




class SavingsMinimalSerializer(serializers.ModelSerializer):
    member = MemberUserSerializer()
    savings_type = SavingsTypeSerializer()

    class Meta:
        model = Savings
        fields = ('id','member','amount','date','savings_type')


class SavingsDepositMinimalSerializer(serializers.ModelSerializer):
    member = MemberUserSerializer()
    #savings_type = SavingsTypeSerializer()

    class Meta:
        model = SavingsDeposit
        fields = ('id','member','amount','date','savings_type')


class SavingsWithdrawalMinimalSerializer(serializers.ModelSerializer):
    member = MemberUserSerializer()
    #savings_type = SavingsTypeSerializer()

    class Meta:
        model = SavingsDeposit
        fields = ('id','member','amount','date','savings_type')