from django.urls import path

from . import views
from .views import RiskTypeView, RiskTypeDetailView

urlpatterns = [
    path("risktypes/", RiskTypeView.as_view(), name="get-all-riskTypes"),
    path(
        "risktypes/<int:pk>", RiskTypeDetailView.as_view(),
        name="get-riskType"
    ),
]
