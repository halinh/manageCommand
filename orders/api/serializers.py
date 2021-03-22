"""Serializers"""
from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """As documentation explains"""

    class Meta:
        model = Order
        fields = "__all__"
