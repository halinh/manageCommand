"""Filter"""
import datetime

import django_filters
import pytz
from django.forms import DateInput
from django.utils.translation import ugettext_lazy as _

from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    """As documentation explains"""

    id = django_filters.CharFilter(
        label=_("Order Id"),
        required=False,
        field_name="order_id",
        lookup_expr="icontains",
    )
    date_after = django_filters.DateFilter(
        label=_("Order After"),
        required=False,
        field_name="order_purchase_date",
        widget=DateInput(attrs={"type": "date"}),
        method="filter_date_after",
    )
    date_before = django_filters.DateFilter(
        label=_("Order Before"),
        required=False,
        field_name="order_purchase_date",
        widget=DateInput(attrs={"type": "date"}),
        method="filter_date_before",
    )
    amount = django_filters.RangeFilter(
        label=_("Order Amount"), required=False, field_name="order_amount"
    )
    items = django_filters.RangeFilter(
        label=_("Order Items"), required=False, field_name="order_items"
    )
    marketplace = django_filters.CharFilter(
        label=_("Marketplace"),
        required=False,
        field_name="marketplace",
        lookup_expr="icontains",
    )

    class Meta:
        model = Order
        fields = ["id", "date_after", "date_before", "amount", "items", "marketplace"]

    def filter_date_after(self, queryset, _name, value):  # pylint: disable=R0201
        """Filter of orders after a date"""
        value = datetime.datetime.combine(
            value, datetime.time.min, tzinfo=pytz.timezone("utc")
        )
        return queryset.filter(order_purchase_date__gte=value)

    def filter_date_before(self, queryset, _name, value):  # pylint: disable=R0201
        """Filter of orders before a date"""
        value = datetime.datetime.combine(
            value, datetime.time.max, tzinfo=pytz.timezone("utc")
        )
        return queryset.filter(order_purchase_date__lte=value)
