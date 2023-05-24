"""urls"""
from django.urls import include, path
from rest_framework import routers

from .views import BlogViewSet, ImagesViewSet, InstrumentsViewSet, SubCatViewSet
router = routers.DefaultRouter()
router.register(r"instruments", InstrumentsViewSet, basename="instruments")
router.register(r"blog", BlogViewSet, basename="blog")
router.register(r"images", ImagesViewSet, basename="images")
router.register(r'subcategory', SubCatViewSet, basename='subcategory')


urlpatterns = [
    path("api/v1/", include(router.urls)),  # http://127.0.0.1:8000/api/v1/instruments/
]
