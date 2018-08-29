from django.contrib import admin
from .models import RiskType, TextField, NumberField, DateField

# Register your models here.

admin.site.register(RiskType)
admin.site.register(TextField)
admin.site.register(NumberField)
admin.site.register(DateField)
