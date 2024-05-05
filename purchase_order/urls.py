# urls.py
from django.urls import path
from .views import (
    PurchaseOrderListCreate,
    PurchaseOrderRetrieveUpdateDestroy,
    AcknowledgePurchaseOrderView,
)

urlpatterns = [
    path(
        "purchase_orders/",
        PurchaseOrderListCreate.as_view(),
        name="purchase-order-list-create",
    ),
    path(
        "purchase_orders/<int:pk>/",
        PurchaseOrderRetrieveUpdateDestroy.as_view(),
        name="purchase-order-retrieve-update-destroy",
    ),
    path(
        "purchase_orders/<int:pk>/acknowledge/",
        AcknowledgePurchaseOrderView.as_view(),
        name="acknowledge-purchase-order-view",
    ),
]
