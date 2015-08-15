from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from members.models import Member, Group, NextOfKin


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        depth = 1


class MemberUserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.username

    def get_first_name(self,obj):
        return obj.user.first_name

    def get_last_name(self,obj):
        return obj.user.last_name

    class Meta:
        model = Member
        depth = 0
        fields = ('id', 'username', 'first_name', 'last_name')





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
