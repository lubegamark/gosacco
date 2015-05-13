from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from members.models import Member, Group, NextOfKin
from shares.models import ShareType, Shares


class ShareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shares


class ShareTypeSerializer(serializers.ModelSerializer):
    shareType = ShareSerializer(many=True, read_only=True)

    class Meta:
        model = ShareType
        # fields = ()