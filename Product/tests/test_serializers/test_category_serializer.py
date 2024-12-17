from django.test import TestCase

from Product.factories import CategoryFactory
from Product.serializers import CategorySerializer

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data

        self.assertEquals(serializer_data["title"], "food")