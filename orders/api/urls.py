"""Rest URL"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.api.views import OrderCreateAPIView

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("create/", OrderCreateAPIView.as_view(), name="order-create-api"),
]
