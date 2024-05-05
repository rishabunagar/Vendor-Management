from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer, VendorPerformanceSerializer
from rest_framework.permissions import IsAuthenticated


class VendorListCreate(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating vendors.

    Retrieves a list of all vendors or creates a new vendor.
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting vendors.

    Retrieves, updates, or deletes a specific vendor instance.
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


class VendorPerformanceView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving vendor performance metrics.

    Retrieves performance metrics for a specific vendor.
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "vendor_id"
