from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ["id", "user", "product", "quantity", "total_price", "purchased_at"]
        read_only_fields = ["total_price", "purchased_at", "user"]
