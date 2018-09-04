from django.contrib import admin
from .models import RiskType, TextField, NumberField, DateField, EnumField
from .models import EnumFieldValue

# Register your models here.

admin.site.register(RiskType)
admin.site.register(TextField)
admin.site.register(NumberField)
admin.site.register(DateField)
admin.site.register(EnumField)
admin.site.register(EnumFieldValue)
