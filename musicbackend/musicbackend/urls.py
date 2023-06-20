from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from musicbackend import settings
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("instruments.urls")),
    path('accounts/', include('allauth.urls')),
    path('chat/', include('chat.urls')),
    # path(r'^messaging/', include('rest_messaging.urls', namespace='rest_messaging')),
    # path(r'^messaging/centrifugo/', include('rest_messaging_centrifugo.urls', namespace='rest_messaging_centrifugo')),
    # path("instant/", include("instant.urls")),
]

urlpatterns += doc_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
