# urls.py
from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDestroy, VendorPerformanceView

urlpatterns = [
    path("vendors/", VendorListCreate.as_view(), name="vendor-list-create"),
    path(
        "vendors/<int:pk>/",
        VendorRetrieveUpdateDestroy.as_view(),
        name="vendor-retrieve-update-destroy",
    ),
    path(
        "vendors/<int:vendor_id>/performance",
        VendorPerformanceView.as_view(),
        name="vendor-performance-view",
    ),
]
