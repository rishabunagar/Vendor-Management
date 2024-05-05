from django.db.models.signals import post_save
from django.dispatch import receiver

from common.helper import create_unique_no
from purchase_order.models import PurchaseOrder
from vendor.vendor_performance import VendorPerformance


@receiver(post_save, sender=PurchaseOrder)
def purchase_order_creation(sender, created, instance, **kwargs):

    """
    Handle creation of purchase orders and update vendor performance metrics if the order is completed.

    When a purchase order is created:
    - If it's not a new creation and the status is 'completed', update the vendor's performance metrics.
    - If it's a new creation, generate a unique 'po_code' for the purchase order.

    Parameters:
        sender (Model): The model class that sent the signal.
        created (bool): Indicates whether the instance was created or updated.
        instance (PurchaseOrder): The instance of the PurchaseOrder model being saved.
        **kwargs (dict): Additional keyword arguments.
    """

    if not created:
        vendor_performance = VendorPerformance(instance.vendor_id)
        vendor_performance_data = vendor_performance.get_vendor_performance_data()
        instance.vendor.on_time_delivery_rate = vendor_performance_data[
            "on_time_delivery_rate"
        ]
        instance.vendor.quality_rating_avg = vendor_performance_data[
            "quality_rating_avg"
        ]
        instance.vendor.average_response_time = vendor_performance_data[
            "average_response_time"
        ]
        instance.vendor.fulfillment_rate = vendor_performance_data["fulfillment_rate"]
        instance.vendor.save()
    else:
        PurchaseOrder.objects.filter(id=instance.id).update(
            po_code=create_unique_no("PO", instance.id)
        )
