from rest_framework import serializer
from .models import Product

class ProductSerializer(serializer.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']