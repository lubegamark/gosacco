# Create your views here.
from django.http.response import Http404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from loans.models import Loan, LoanApplication, Security
from loans.serializers import SecuritySerializer, LoanApplicationSerializer, LoanSerializer
from members.models import Member


class LoansView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

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
        List all of a Member's Loans
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        loans = Loan.get_members_loans(member)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)


class LoanApplicationView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

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
        List Member's Loan Applications
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        applications = LoanApplication.get_members_loan_applications(member)
        serializer = LoanApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    #TODO Implement Method to handle Posting Loan Application
    # def post(self, request, pk, format=None):
    #     """
    #     Make A Loan Application
    #     """
    #     pass


class SecurityView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

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
        List Member's Securities
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        securities = Security.get_members_securities(member)
        serializer = SecuritySerializer(securities, many=True)
        return Response(serializer.data)

    #TODO Implement Method to handle Posting New Security
    # def post(self, request, pk, format=None):
    #     """
    #     Add a Loan Security
    #     """
    #     pass
