from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/", include("django_crg_api.urls")),
    path("", include("django_crg_frontend.urls")),
]
