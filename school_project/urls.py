"""
URL configuration for school_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django project
# school_project/urls.py

from django.contrib import admin
from django.urls import path, include

# from products import views
# from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Namespace each app under api/
    path('products/', include('products.urls')),
    path('students/', include('students.urls')),
    path('nested-product/', include('nested_product.urls'))

    # Your frontend view
    # path('', views.product_list_view, name='product_list'),
]

