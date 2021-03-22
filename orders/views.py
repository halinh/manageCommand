"""Views"""
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from django_filters.views import FilterView

from orders.filters import OrderFilter
from orders.forms import OrderModelForm
from orders.models import Order


class OrderListView(ListView):  # pylint: disable=too-many-ancestors
    """As documentation explains"""

    template_name = "orders/order_list.html"
    context_object_name = "orders"
    queryset = Order.objects.all()
    paginate_by = 10


class OrderDetailView(DetailView):
    """As documentation explains"""

    template_name = "orders/order_detail.html"
    context_object_name = "order"

    def get_object(self):  # pylint: disable=W0221
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order, id=id_)


class OrderFilterView(FilterView):  # pylint: disable=too-many-ancestors
    """As documentation explains"""

    filterset_class = OrderFilter
    template_name = "orders/order_form.html"
    context_object_name = "orders"
    paginate_by = 10


class OrderCreateView(CreateView):
    """As documentation explains"""

    template_name = "orders/order_create.html"
    form_class = OrderModelForm

    def form_valid(self, form=1):
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    """As documentation explains"""

    template_name = "orders/order_update.html"
    form_class = OrderModelForm

    def get_object(self):  # pylint: disable=W0221
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order, id=id_)

    def form_valid(self, form=1):
        return super().form_valid(form)


class OrderDeleteView(DeleteView):
    """As documentation explains"""

    template_name = "orders/order_delete.html"
    context_object_name = "order"

    def get_object(self):  # pylint: disable=W0221
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order, id=id_)

    def get_success_url(self):
        return reverse("orders:order-list")
