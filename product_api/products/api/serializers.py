from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['slug', 'title', 'desc', 'price', 'is_active', 'created_at', 'updated_at']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'slug', 'title', 'desc', 'price', 'is_active', 'created_at', 'updated_at']
