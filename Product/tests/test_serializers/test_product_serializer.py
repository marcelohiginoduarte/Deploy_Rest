from django.test import TestCase
from Product.factories import CategoryFactory, productFactory
from Product.serializers import ProductSerializer

class TestProductSerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="technology")
        self.product_1 = productFactory(title="mouse", price=100)
        self.product_1.categories.set([self.category])
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["title"], "mouse")
        self.assertEqual(
            serializer_data["categories"][0]["title"], "technology"
        )

    def test_create_product_with_categories(self):
        category = CategoryFactory(title="hardware")
        data = {
            "title": "keyboard",
            "price": 50,
            "categories_id": [category.id],
        }

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save()
            self.assertEqual(product.title, "keyboard")
            self.assertEqual(product.categories.count(), 1)  
            self.assertEqual(product.categories.first().title, "hardware")