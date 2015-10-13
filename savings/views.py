# Create your views here.
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from members.models import Member
from savings.models import Savings, SavingsType, SavingsWithdrawal, SavingsDeposit
from savings.serializers import SavingsSerializer, SavingsTypeSerializer, SavingsWithdrawSerializer, SavingsDepositSerializer, CreateSavingsSerializer, \
    SavingsMinimalSerializer, SavingsDepositMinimalSerializer, SavingsWithdrawalMinimalSerializer, \
    SavingsTransactionsMinimalSerializer
from rest_framework import generics

# class SavingsList(APIView):

#     def get(self, request, format=None ):
#         """
#         A list of Savings
#         """
#         savings = Savings.objects.all()
#         serializer = SavingsSerializer(savings, many=True)
#         return Response(serializer.data)


class SavingsList(APIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer

class SavingsCreate(generics.CreateAPIView):
    queryset = Savings.objects.all()
    serializer_class = CreateSavingsSerializer

class SavingsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Savings.objects.all()
    serializer_class = CreateSavingsSerializer

class SavingsTypeList(generics.ListCreateAPIView):
    queryset = SavingsType.objects.all()
    serializer_class = SavingsTypeSerializer

class SavingsTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavingsType.objects.all()
    serializer_class = SavingsTypeSerializer

class SavingsWithdrawList(generics.ListCreateAPIView):
    queryset = SavingsWithdrawal.objects.all()
    serializer_class = SavingsWithdrawSerializer

class SavingsWithdrawDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavingsWithdrawal.objects.all()
    serializer_class = SavingsWithdrawSerializer

class SavingsDepositList(generics.ListCreateAPIView):
    queryset = SavingsDeposit.objects.all()
    serializer_class = SavingsDepositSerializer

class SavingsDepositDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavingsDeposit.objects.all()
    serializer_class = SavingsDepositSerializer



class SavingsView(APIView):
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
        List Member's savings
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        savings = Savings.get_members_savings(member)
        serializer = SavingsMinimalSerializer(savings, many=True)
        return Response(serializer.data)


class SavingsDepositView(APIView):
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
        deposits = SavingsDeposit.get_savings_deposits(member)
        serializer = SavingsDepositMinimalSerializer(deposits, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        """
        Deposit Memeber's Savings
        """
        member = self.get_member(pk)
        new_savings_details = request.data
        savings_type = SavingsType.objects.get(pk=new_savings_details['share_type'])
        amount = new_savings_details['amount']
        savings_added = SavingsDeposit.make_savings(member=member, savings_type=savings_type, amount=amount)

        if savings_added:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SavingsWithdrawalView(APIView):
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
        deposits = SavingsWithdrawal.get_withdrawals(member)
        serializer = SavingsWithdrawalMinimalSerializer(deposits, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        """
        Deposit Memeber's Savings
        """
        member = self.get_member(pk)
        new_savings_details = request.data
        savings_type = SavingsType.objects.get(pk=new_savings_details['savings_type'])
        amount = new_savings_details['amount']
        savings_withdrawn = SavingsWithdrawal.withdraw_savings(member=member, savings_type=savings_type, amount=amount)

        if savings_withdrawn:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SavingsTransactionsView(APIView):
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
        transactions = Savings.get_savings_transactions(member)
        serializer = SavingsTransactionsMinimalSerializer(transactions, many=True)
        return Response(serializer.data)