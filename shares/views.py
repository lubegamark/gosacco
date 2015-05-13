# Create your views here.
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from members.models import Member
from shares.models import Shares, ShareType, SharePurchase
from shares.serializers import SharesSerializer


class ShareList(APIView):
    """
    Show a members different shares (totals).
    """
    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404


    def get(self,  request, member_pk, format=None):
        """
        List members shares
        """
        member =  self.get_member(int(member_pk))
        shares = Shares.get_members_shares(member, )
        serializer = SharesSerializer(shares, many=True)
        return Response(serializer.data)

    def post(self, request, member_pk, format=None):
        """
        Add a new share for a user
        """
        member = self.get_member(member_pk)
        new_share_details = request.data
        share_type = ShareType.objects.get(pk=new_share_details['share_type'])
        #serializer = SharesSerializer(data=request.data)
        shares_added = SharePurchase.issue_shares(member, new_share_details['number_of_shares'], share_type)

        if shares_added:
            #serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)