from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """
        Serializer for PurchaseOrder model.

        Includes all fields of the PurchaseOrder model and adds a read-only field 'po_code'.
    """
    po_code = serializers.CharField(read_only=True)
    quality_rating = serializers.FloatField(required=False)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class AcknowledgePurchaseOrderSerializer(serializers.ModelSerializer):
    """
        Serializer for acknowledging a PurchaseOrder.

        Includes only the 'acknowledgment_date' field for updating the acknowledgment date of a PurchaseOrder.
    """
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgment_date']