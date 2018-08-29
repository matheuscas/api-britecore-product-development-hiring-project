from django.db import models

# Create your models here.

class RiskType(models.Model):
    description = models.CharField(max_length=200)

class Field(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        abstract = True

class TextField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="text_fields", on_delete=models.CASCADE)
    value = models.CharField(max_length=200, blank=True)

class NumberField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="number_fields", on_delete=models.CASCADE)
    value = models.FloatField(blank=True, null=True)

class DateField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="date_fields", on_delete=models.CASCADE)
    value = models.DateField(blank=True, null=True)

class EnumField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="enum_fields", on_delete=models.CASCADE)

class EnumFieldValue(models.Model):
    enum_field = models.ForeignKey(EnumField, related_name="enum_field_values", on_delete=models.CASCADE)
    key = models.IntegerField()
    value = models.CharField(max_length=100)
