from rest_framework import serializers
from .models import RiskType

class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields = '__all__'