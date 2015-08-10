from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

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


class GroupSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    leader = serializers.StringRelatedField()

    class Meta:
        model = Group


class GroupMemberSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        # fields = ()


class NextOfKinSerializer(serializers.ModelSerializer):

    class Meta:
        model = NextOfKin


class MemberViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        """
        Return a list of objects.

        """
        return super(MemberViewSet, self).list(request, *args, **kwargs)