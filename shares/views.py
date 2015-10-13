# Create your views here.
from django.http.response import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from members.models import Member
from shares.models import Shares, ShareType, SharePurchase, ShareTransfer
from shares.serializers import SharesSerializer,ShareTypeSerializer, SharePurchaseSerializer, ShareTransferSerializer, \
    SharesMinimalSerializer, ShareTransactionsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

class ShareList(APIView):

    def get(self, request, format=None):
        """
        Show a list of shares
        """
        shares = Shares.objects.all()
        serializer = SharesSerializer(shares,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        """
        Add new share
        """
        serializer = SharesSerializer(data=request.DATA)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShareDetail(APIView):
    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self,  request, pk, format=None):
        """
        Show Member's shares
        """
        member = self.get_member(int(pk))
        shares = Shares.get_members_shares(member, )
        serializer = SharesMinimalSerializer(shares, many=True)
        return Response(serializer.data)


class ShareTypeList(APIView):
    def get(self, request, format=None):
        """
        List the share types
        """
        sharetype = ShareType.objects.all()
        serializer = ShareTypeSerializer(sharetype, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        """
        Add a share type
        """
        serializer = ShareTypeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SharePurchaseList(APIView):
    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        List the Share Purchase Transactions
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        sharepurchase = SharePurchase.get_share_purchases(members=member)
        serializer = SharePurchaseSerializer(sharepurchase, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Purchase a share
        """
        serializer = SharePurchaseSerializer(data=request.DATA)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShareTransferList(APIView):
    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        List Share Transfer Transactions
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        sharetransfer = ShareTransfer.get_share_transfers(members=member)
        serializer = ShareTransferSerializer(sharetransfer, many=True)
        return Response(serializer.data)


class ShareTransactionsView(APIView):
    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self,  request, pk, format=None):
        """
        List Member's savings Deposits
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        transactions = Shares.get_share_transactions(member)
        serializer = ShareTransactionsSerializer(transactions, many=True)
        return Response(serializer.data)