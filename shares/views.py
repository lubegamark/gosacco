# Create your views here.
from django.http.response import Http404
from rest_framework import status, generics
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from members.models import Member
from shares.models import Shares, ShareType, SharePurchase, ShareTransfer
from shares.serializers import SharesSerializer,ShareTypeSerializer, SharePurchaseSerializer, ShareTransferSerializer, \
    SharesMinimalSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

class ShareList(APIView):

    def get(self, request, format=None):
        """
        Show are list of shares
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
    """
    Handles all deltails about a users shares
    """
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
        List members shares
        """
        member = self.get_member(int(pk))
        shares = Shares.get_members_shares(member, )
        serializer = SharesMinimalSerializer(shares, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        """
        Add a new share for a user
        """
        member = self.get_member(pk)
        new_share_details = request.data
        share_type = ShareType.objects.get(pk=new_share_details['share_type'])
        #serializer = SharesSerializer(data=request.data)
        shares_added = SharePurchase.issue_shares(member, new_share_details['number_of_shares'], share_type)

        if shares_added:
            #serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ShareTypeList(generics.ListCreateAPIView):
    """
    List the share types
    """
    queryset = ShareType.objects.all()
    serializer_class = ShareTypeSerializer
    # def get(self, request, format=None):
    #     sharetype = ShareType.objects.all()
    #     serializer = ShareTypeSerializer(sharetype, many=True)
    #     return Response(serializer.data)
    # @csrf_exempt
    # def post(self, request, format=None):
    #     """
    #     Add a share type
    #     """
    #     serializer = ShareTypeSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SharePurchaseList(generics.ListCreateAPIView):
    """
     List the share types
    """
    # def get(self, request, format=None):
    #     sharepurchase = SharePurchase.objects.all()
    #     serializer = SharePurchaseSerializer(sharepurchase, many=True)
    #     return Response(serializer.data)
    #
    # """ Purchase a share"""
    # @csrf_exempt
    # def post(self, request, format=None):
    #     serializer = SharePurchaseSerializer(data=request.DATA)
    #     if serializer.is_valid:
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = SharePurchase.objects.all()
    serializer_class = SharePurchaseSerializer

    def get(self, request, format=None):
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
        List of Share Transfers
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        sharetransfer = ShareTransfer.get_share_transfers(members=member)
        serializer = ShareTransferSerializer(sharetransfer, many=True)
        return Response(serializer.data)
