"""Forms"""
from django import forms
from django.forms import DateInput
from django.utils.translation import ugettext_lazy as _

from orders.models import Order


class OrderModelForm(forms.ModelForm):
    """As documentation explains"""

    order_purchase_date = forms.DateField(
        label=_("Order Purchase Date"),
        required=False,
        widget=DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Order
        fields = "__all__"

    field_order = [
        "order_id",
        "order_purchase_date",
        "order_amount",
        "order_items",
        "marketplace",
    ]
