"""
URL configuration for atomic_disciple_making_ministry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from allauth.account.views import PasswordResetView
from django.urls import path, include


urlpatterns = [
    # Django admin
    path("atomic-admin/", admin.site.urls),
    # User management
    path(
        "accounts/password/reset/",
        PasswordResetView.as_view(),
        name="reset_password",
    ),
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("pages.urls")),
    path("aboutus/", include("aboutus.urls")),
    path("contactus/", include("contactus.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
