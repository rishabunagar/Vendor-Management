from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """
    Serializer for Vendor model.

    Includes fields 'id', 'name', 'email', 'vendor_code', 'contact_details', and 'address'.
    The 'vendor_code' field is read-only.
    """

    vendor_code = serializers.CharField(read_only=True)

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Enter your password here",
        style={"input_type": "password", "placeholder": "Password"},
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Enter your confirm password here",
        style={"input_type": "password", "placeholder": "Password"},
    )

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password is not match here."}
            )

        return data

    def create(self, validated_data):
        vendor = super().create(validated_data)
        vendor.set_password(validated_data["password"])
        vendor.save()
        return vendor

    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "email",
            "password",
            "confirm_password",
            "vendor_code",
            "contact_details",
            "address",
        ]


class VendorPerformanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Vendor performance metrics.

    Includes fields 'id', 'name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
    'average_response_time', and 'fulfillment_rate'.
    """

    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
