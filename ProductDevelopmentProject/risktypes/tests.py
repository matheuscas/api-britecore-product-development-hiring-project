from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import RiskType, TextField, NumberField, DateField, EnumField
from .models import EnumFieldValue
from .serializers import RiskTypeSerializer
from random import randint

# Create your tests here.


class BaseViewTests(APITestCase):
    client = APIClient()

    @staticmethod
    def create_risk_types(risk_type_desc):
        risk_type = RiskType.objects.create(description=risk_type_desc)
        for iterr in list(range(0, randint(1, 9))):
            TextField.objects.create(
                name=f'risk_type_{risk_type.id}_text_field_{iterr}',
                risk_type=risk_type
            )
        for iterr in list(range(0, randint(1, 9))):
            NumberField.objects.create(
                name=f'risk_type_{risk_type.id}_number_field_{iterr}',
                risk_type=risk_type
            )
        for iterr in list(range(0, randint(1, 9))):
            DateField.objects.create(
                name=f'risk_type_{risk_type.id}_date_field_{iterr}',
                risk_type=risk_type
            )
        enum_field = EnumField.objects.create(
            name=f'risk_type_{risk_type.id}_enum_field_{iterr}',
            risk_type=risk_type
        )

        for iterr in list(range(0, randint(2, 29))):
            EnumFieldValue.objects.create(
                value=f'enum_value_{enum_field.id}_enum_field_{iterr}',
                enum_field=enum_field
            )

    def setUp(self):
        self.create_risk_types("Gold Tournament Prize")
        self.create_risk_types("Automobile Policy")
        self.create_risk_types("Cyber Liability Coverage")


class GetAllRiskTypes(BaseViewTests):
    def test_get_all_risk_types(self):
        """
        This test ensures that all risk types added in the setUp method
        exist when a GET request is executed to the risktypes/ endpoint
        """

        response = self.client.get(
            reverse("get-all-riskTypes", kwargs={"version": "v1"})
        )

        expected = RiskType.objects.all()
        serialized = RiskTypeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_risk_type(self):
        risk_types = RiskType.objects.all()
        expected_risk_type = risk_types[0]
        expected_risk_type_serialized = RiskTypeSerializer(expected_risk_type)
        response = self.client.get(
            reverse("get-riskType", kwargs={
                "version": "v1",
                "pk": expected_risk_type.pk
            })
        )
        self.assertEqual(response.data, expected_risk_type_serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
