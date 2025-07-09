from django.shortcuts import render

from .models import Product, Review
from .serializers import ProductSerializers, ReviewSerializers

from rest_framework import viewsets, status
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 0:
            return Response({'error': 'can not delete the product because of more than 0 stock'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
    
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializers

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
