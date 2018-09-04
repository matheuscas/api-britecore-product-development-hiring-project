from rest_framework import serializers
from .models import RiskType, EnumField


class EnumFieldSerializer(serializers.ModelSerializer):

    enum_field_values = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='value'
    )

    class Meta:
        model = EnumField
        fields = ('name', 'enum_field_values')


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

    enum_fields = EnumFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = '__all__'
