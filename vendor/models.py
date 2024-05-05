from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import Base
from vendor.manager import VendorManager


class Vendor(AbstractUser, Base):
    username = None
    email = models.EmailField("email address", unique=True)
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = VendorManager()

    def __str__(self):
        return self.email
