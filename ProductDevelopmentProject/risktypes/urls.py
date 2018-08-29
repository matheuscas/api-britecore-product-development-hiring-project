from django.urls import path

from . import views
from .views import RiskTypeView

urlpatterns = [
    path('risktypes', RiskTypeView.as_view(), name='get-riskTypes')
]