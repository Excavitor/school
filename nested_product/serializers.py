from .models import Product, Review
from decimal import Decimal
from rest_framework import serializers

vat_in_percentage = Decimal('5')

class ProductSerializers(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'product_status', 'price', 'price_with_tax', 'stock', 'created_at']
        read_only_fields = ['id', 'price_with_tax', 'created_at']

    def get_price_with_tax(self, obj):
        vat = vat_in_percentage / Decimal('100')
        vat_on_price = obj.price + (vat * obj.price)

        return vat_on_price


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'name', 'description','product_id']
        read_only_fields = ['id', 'product_id']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)