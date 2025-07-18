from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        # print(product)
        # print(product.stock)
        if product.stock < 1:
            return Response({'error': 'Cannot update product with zero stock.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 0:
            return Response({'error': 'Only products with 0 stock can be deleted.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)
