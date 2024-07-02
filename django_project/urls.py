from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("randomin/", admin.site.urls),
    # path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls", namespace="pages")),
]

if settings.INCLUDE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
