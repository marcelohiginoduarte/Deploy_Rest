from django.test import TestCase
import pytest
from Product.factories import CategoryFactory, productFactory
from Product.serializers import CategorySerializer

@pytest.mark.django_db
class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data

        self.assertEqual(serializer_data["title"], "food")