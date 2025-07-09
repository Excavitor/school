from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter
from .views import ProductViewSet, product_list_view

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('rest-api/', include(router.urls)),
]