from rest_framework.viewsets import ModelViewSet

from Product.models import Product
from Product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")
