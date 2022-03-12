from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Heartbeat


urlpatterns = [
    path("", include('users.urls')),
    path("heartbeat/", Heartbeat.as_view(), name='heartbeat'),
    # django admin routes
    path('admin/', admin.site.urls),
    # users API
    path("api/users/", include('users.api.urls')),
    # oauth2 crud routes
    path('oauth2/', include('oauth2.urls', namespace='oauth2'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
