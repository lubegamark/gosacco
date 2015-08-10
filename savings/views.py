# Create your views here.
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from savings.models import Savings, SavingsType, SavingsWithdrawal, SavingsPurchase
from savings.serializers import SavingsSerializer, SavingsTypeSerializer, SavingsWithdrawSerializer, SavingsPurchaseSerializer, CreateSavingsSerializer
from rest_framework import generics

# class SavingsList(APIView):

#     def get(self, request, format=None ):
#         """
#         A list of Savings
#         """
#         savings = Savings.objects.all()
#         serializer = SavingsSerializer(savings, many=True)
#         return Response(serializer.data)

class SavingsList(generics.ListAPIView):
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

class SavingsPurchaseList(generics.ListCreateAPIView):
	queryset = SavingsPurchase.objects.all()
	serializer_class = SavingsPurchaseSerializer

class SavingsPurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SavingsPurchase.objects.all()
	serializer_class = SavingsPurchaseSerializer
