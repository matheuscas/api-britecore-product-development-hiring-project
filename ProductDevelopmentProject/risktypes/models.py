from django.db import models

# Create your models here.

class RiskType(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.description}'

class Field(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'

class TextField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="text_fields", on_delete=models.CASCADE)

class NumberField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="number_fields", on_delete=models.CASCADE)

class DateField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="date_fields", on_delete=models.CASCADE)

class EnumField(Field):
    risk_type = models.ForeignKey(RiskType, related_name="enum_fields", on_delete=models.CASCADE)

class EnumFieldValue(models.Model):
    enum_field = models.ForeignKey(EnumField, related_name="enum_field_values", on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.value}'
