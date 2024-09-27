from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from main.views import under_construction

urlpatterns = [
    path("", include("main.urls")),
    path("collection", include("collection.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    re_path(r'^.*$', under_construction),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
