# students/urls.py

from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from .views import StudentViewSet, student_list_view, ReviewViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='student')

review_router = routers.NestedDefaultRouter(router, 'students', lookup = 'student')
review_router.register('reviews', ReviewViewSet, basename='student-review')

urlpatterns = [
    path('', student_list_view, name='student-list'),
    path('rest-api/', include(router.urls)),
    path('rest-api/', include(review_router.urls)),
]

