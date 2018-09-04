from django.shortcuts import render
from rest_framework import generics

from .models import RiskType
from .serializers import RiskTypeSerializer

# Create your views here.


class RiskTypeView(generics.ListAPIView):
    """
    Return a list of all existing risk types
    """
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


class RiskTypeDetailView(generics.RetrieveAPIView):
    """
    Return a risk type based on the provided id
    """
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
