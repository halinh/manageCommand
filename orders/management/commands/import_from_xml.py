"""Django command to import data."""
from datetime import datetime

import requests
import xmltodict
from django.core.management.base import BaseCommand, CommandError

from orders.models import Order


class Command(BaseCommand):
    """Import data from API to populate the database."""

    help = "Import data from API to populate the database."

    def handle(self, *args, **options):
        response = requests.get("http://test.lengow.io/orders-test.xml")
        xml_reader = response.content.decode("utf-8", errors="ignore")
        orders_test = xmltodict.parse(xml_reader)
        orders = orders_test["statistics"]["orders"]
        for order in orders.items():
            for item in order[1]:
                order_id = item["order_id"]
                if item["order_purchase_date"]:
                    order_purchase_date = datetime.strptime(
                        item["order_purchase_date"], "%Y-%m-%d"
                    ).date()
                else:
                    order_purchase_date = None
                if item["order_amount"]:
                    order_amount = float(item["order_amount"])
                else:
                    order_amount = None
                if item["order_items"]:
                    order_items = int(item["order_items"])
                else:
                    order_items = None
                marketplace = item["marketplace"]
                _, created = Order.objects.get_or_create(
                    order_id=order_id,
                    order_purchase_date=order_purchase_date,
                    order_amount=order_amount,
                    order_items=order_items,
                    marketplace=marketplace,
                )
