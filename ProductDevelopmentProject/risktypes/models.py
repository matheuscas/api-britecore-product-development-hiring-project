from django.db import models

# Create your models here.

class RiskType(models.Model):
    description = models.CharField(max_length=200)

class Field(models.Model):
    riskType = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    class Meta:
        abstract = True

class TextField(Field):
    value = models.CharField(max_length=200, blank=True)

class NumberField(Field):
    value = models.FloatField(blank=True, null=True)

class DateField(Field):
    value = models.DateField(blank=True, null=True)

class EnumField(Field):
    pass

class EnumFieldValue(models.Model):
    enumField = models.ForeignKey(EnumField, on_delete=models.CASCADE)
    key = models.IntegerField()
    value = models.CharField(max_length=100)
