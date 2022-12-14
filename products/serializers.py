from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['id', 'title', 'description', 'inventory_quantity', 'price']
