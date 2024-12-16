from django.urls import path, include
from rest_framework.routers import SimpleRouter

from order.viewset.order_viewset import OrderViewSet


router = SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls))
]