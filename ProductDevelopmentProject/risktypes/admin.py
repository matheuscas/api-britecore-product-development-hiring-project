from django.contrib import admin
from .models import RiskType, TextField, NumberField, DateField, EnumField
from .models import EnumFieldValue

# Register your models here.


class TextFieldInline(admin.StackedInline):
    model = TextField
    extra = 0


class DateFieldInline(admin.StackedInline):
    model = DateField
    extra = 0


class NumberFieldInline(admin.StackedInline):
    model = NumberField
    extra = 0


class EnumFieldValueInline(admin.StackedInline):
    model = EnumFieldValue
    extra = 0


class EnumFieldInline(admin.StackedInline):
    model = EnumField
    extra = 0


@admin.register(EnumField)
class EnumFieldAdmin(admin.ModelAdmin):
    inlines = [
        EnumFieldValueInline
    ]


@admin.register(RiskType)
class RiskTypeAdmin(admin.ModelAdmin):
    fields = ["description"]
    inlines = [
        TextFieldInline,
        DateFieldInline,
        NumberFieldInline,
        EnumFieldInline
    ]
