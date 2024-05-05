from django.db.models.signals import post_save
from django.dispatch import receiver

from common.helper import create_unique_no
from vendor.models import Vendor


@receiver(post_save, sender=Vendor)
def vendor_creation(sender, created, instance, **kwargs):
    if created:
        instance.vendor_code = create_unique_no("VE", instance.id)
        instance.save()
