from rest_framework import serializers
from Product.models import Category
from Product.models.product import Product
from Product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True 
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "categories",
            "categories_id",
        ]

    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")
        product = Product.objects.create(**validated_data)
        product.categories.set(category_data)
        return product