from purchase_order.models import PurchaseOrder
from django.db.models import F, Avg


class VendorPerformance:
    """
    Utility class for calculating performance metrics for a vendor based on their purchase orders.

    Attributes:
        vendor_id (int): The ID of the vendor for which performance metrics are calculated.
    """

    def __init__(self, vendor_id):
        """
        Initializes the VendorPerformance instance with the vendor's ID.

        Args:
            vendor_id (int): The ID of the vendor for which performance metrics are calculated.
        """
        self.vendor_id = vendor_id
        self.get_all_completed_purchase_orders_count = (
            self.get_all_completed_purchase_orders().count()
        )
        self.vendor_before_completed_purchase_orders = (
            self.get_before_completed_purchase_orders().count()
        )
        self.get_fulfillment_purchase_orders_count = (
            self.get_fulfillment_purchase_orders().count()
        )

    def get_vendor_purchase_orders(self):
        """
        Retrieves all purchase orders associated with the vendor.
        """
        return PurchaseOrder.objects.filter(vendor_id=self.vendor_id)

    def get_all_completed_purchase_orders(self):
        """
        Retrieves all completed purchase orders for the vendor.
        """
        return self.get_vendor_purchase_orders().filter(status="completed")

    def get_before_completed_purchase_orders(self):
        """
        Retrieves completed purchase orders delivered on time
        """
        return self.get_all_completed_purchase_orders().filter(
            delivery_date__lte=F("acknowledgment_date")
        )

    def get_acknowledged_purchase_orders(self):
        """
        Retrieves purchase orders acknowledged by the vendor
        """
        return self.get_vendor_purchase_orders().filter(
            acknowledgment_date__isnull=False
        )

    def get_fulfillment_purchase_orders(self):
        """
        Retrieves fulfilled purchase orders.
        """
        return self.get_all_completed_purchase_orders().filter(
            quality_rating__isnull=False
        )

    def get_on_time_delivery_rate(self):
        """
        Calculates the percentage of on-time deliveries.
        """
        return (
            (
                    self.vendor_before_completed_purchase_orders
                    / self.get_all_completed_purchase_orders_count
            )
            * 100
            if self.get_all_completed_purchase_orders_count
            else 0
        )

    def get_quality_rating_avg(self):
        """
        Calculates the average quality rating of completed purchase orders.
        """
        return (
                self.get_all_completed_purchase_orders().aggregate(Avg("quality_rating"))[
                    "quality_rating__avg"
                ]
                or 0
        )

    def get_average_response_time(self):
        """
        Calculates the average response time of acknowledged purchase orders.
        """

        average_response = self.get_acknowledged_purchase_orders().aggregate(
            average_response=Avg(F("acknowledgment_date") - F("issue_date"))
        )["average_response"]

        return average_response.days if average_response and average_response.days > 0 else 0

    def get_fulfillment_rate(self):
        """
        Calculates the fulfillment rate of purchase orders.
        """
        return (
            (
                    self.get_fulfillment_purchase_orders_count
                    / self.get_all_completed_purchase_orders_count
            )
            * 100
            if self.get_all_completed_purchase_orders_count
            else 0
        )

    def get_vendor_performance_data(self):
        """
        Returns a dictionary containing all calculated performance metrics.
        """
        return {
            "on_time_delivery_rate": self.get_on_time_delivery_rate(),
            "quality_rating_avg": self.get_quality_rating_avg(),
            "average_response_time": self.get_average_response_time(),
            "fulfillment_rate": self.get_fulfillment_rate(),
        }
