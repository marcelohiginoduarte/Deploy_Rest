from rest_framework import serializers

from Product.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "title",
            "slug",
            "description",
            "active",
        ]
        extra_kwargs = {"slug": {"required": False}}