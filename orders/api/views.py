"""API Views"""
from rest_framework import generics

from orders.api.serializers import OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    """As documentation explains"""

    serializer_class = OrderSerializer
