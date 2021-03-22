"""Models"""
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    """As documentation explains"""

    order_id = models.CharField(_("Order Id"), blank=True, null=True, max_length=60)
    order_purchase_date = models.DateField(_("Order Purchase Date"), null=True)
    order_amount = models.FloatField(_("Order Amount"), blank=True, null=True)
    order_items = models.PositiveIntegerField(_("Order Items"), blank=True, null=True)
    marketplace = models.CharField(
        _("Marketplace"), blank=True, null=True, max_length=60
    )

    def get_absolute_url(self):  # pylint: disable=R0201
        """Get absolute url"""

        return reverse("orders:order-list")
