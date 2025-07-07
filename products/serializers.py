# products/serializers.py

from decimal import Decimal
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'price_with_tax', 'stock', 'created_at']
        read_only_fields = ['id', 'created_at', 'price_with_tax']

    def get_price_with_tax(self, product):
        tax_rate = Decimal('1.15')
        price_with_tax = product.price * tax_rate
        
        return price_with_tax
