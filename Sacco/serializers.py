from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from Sacco.models import Member, Group, NextOfKin


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        depth = 0



class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group



class NextOfKinSerializer(serializers.ModelSerializer):

    class Meta:
        model = NextOfKin


class MemberViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        """
        Return a list of objects.

        """
        return super(MemberViewSet, self).list(request, *args, **kwargs)