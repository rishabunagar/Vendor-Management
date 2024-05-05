from django.db import models
from vendor.models import Vendor


class PurchaseOrder(models.Model):
    ORDER_STATUS = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_code = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    status = models.CharField(choices=ORDER_STATUS, max_length=30, default="pending")
    quantity = models.IntegerField()
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Order - {self.po_code}"
