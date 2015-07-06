# Create your views here.
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from savings.models import Savings
from savings.serializers import SavingsSerializer


class SavingsList(APIView):

    def get(self, request, format=None ):
        """
        A list of Savings
        """
        savings = Savings.objects.all()
        serializer = SavingsSerializer(savings, many=True)
        return Response(serializer.data)

