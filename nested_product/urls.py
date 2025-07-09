from django.urls import path, include
from .views import ProductViewSet, ReviewViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + product_router.urls
