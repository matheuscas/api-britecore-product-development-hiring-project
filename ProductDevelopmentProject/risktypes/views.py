from django.shortcuts import render
from rest_framework import generics

from .models import RiskType
from .serializers import RiskTypeSerializer

# Create your views here.


class RiskTypeView(generics.ListAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


class RiskTypeDetailView(generics.RetrieveAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
