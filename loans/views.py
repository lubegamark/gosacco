# Create your views here.
from loans.models import LoanApplication
from loans.serializers import LoanApplicationSerializer
from rest_framework import generics

class LoanApplicationList(generics.ListAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
