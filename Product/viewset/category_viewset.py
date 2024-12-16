import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from rest_framework.viewsets import ModelViewSet

from Product.serializers.category_serializer import CategorySerializer
from Product.factories import CategoryFactory
from Product.models import Category


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")