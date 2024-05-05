from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models.signals import post_save

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer, AcknowledgePurchaseOrderSerializer


class PurchaseOrderListCreate(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating purchase orders.

    Retrieves a list of all purchase orders or creates a new purchase order.
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]


class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting purchase orders.

    Retrieves, updates, or deletes a specific purchase order instance.
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]


class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    """
    API endpoint for acknowledging purchase orders.

    Allows vendors to acknowledge purchase orders by updating the acknowledgment date.
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgePurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        """
        Handle the update action when acknowledging a purchase order.
        """
        instance = self.get_object()
        instance.acknowledgment_date = request.data["acknowledgment_date"]
        instance.save()
        post_save.send(PurchaseOrder, instance=instance, created=False)
        return Response({"success": "PO acknowledged successfully"})
