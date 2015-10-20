from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import Http404
from django.contrib.auth.models import User

from members.models import Member, Group
from members.permissions import IsOwnerOrAdmin
from members.serializers import MemberSerializer, GroupSerializer, GroupMemberSerializer, UserSerializer, \
    MemberUserSerializer


class MemberList(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, format=None):
        """
        List all members
        """
        members = Member.objects.all()
        serializer = MemberUserSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Add a new member
        """
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupList(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, format=None):
        """
        List groups.
        """
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new group.
        """
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a Member.
        """
        member = self.get_member(pk)
        self.check_object_permissions(request, member)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit a Member.
        """
        member = self.get_member(pk)
        self.check_object_permissions(request, member)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a Member.
        """
        member = self.get_member(pk)
        self.check_object_permissions(request, member)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupDetail(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_group(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a Group.
        """
        group = self.get_group(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit a Group Member.
        """
        group = self.get_group(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Remove a Group Member.
        """
        group = self.get_group(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupMember(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_groupmember(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a Group Member.
        """
        groupmember = self.get_groupmember(pk)
        serializer = GroupMemberSerializer(groupmember)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit a Group Member.
        """
        groupmember = self.get_groupmember(pk)
        serializer = GroupMemberSerializer(groupmember, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a Group Member.
        """
        groupmember = self.get_groupmember(pk)
        groupmember.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
