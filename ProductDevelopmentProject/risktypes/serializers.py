from rest_framework import serializers
from .models import RiskType

class RiskTypeSerializer(serializers.ModelSerializer):
    text_fields = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    number_fields = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    date_fields = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    enum_fields = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = RiskType
        fields = '__all__'