from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from instruments.views import *
from musicbackend import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('instruments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

