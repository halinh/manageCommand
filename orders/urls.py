"""Urls of the module orders"""
from django.urls import include, path

from orders.views import (OrderCreateView, OrderDeleteView, OrderDetailView,
                          OrderFilterView, OrderListView, OrderUpdateView)

app_name = "orders"

urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("<int:id>/", OrderDetailView.as_view(), name="order-detail"),
    path("search/", OrderFilterView.as_view(), name="order-form"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("<int:id>/update/", OrderUpdateView.as_view(), name="order-update"),
    path("<int:id>/delete/", OrderDeleteView.as_view(), name="order-delete"),
    path("api/", include("orders.api.urls")),
]
