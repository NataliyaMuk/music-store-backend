from django.urls import path, include
from .views import *


from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'instruments', InstrumentsViewSet, basename='instruments')


urlpatterns = [
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/instruments/
]
