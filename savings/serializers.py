from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from savings.models import Savings, SavingsType, SavingsPurchase, SavingsWithdrawal


class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings