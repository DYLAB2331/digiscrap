"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from scrapbook.views import (
    registerView,
    loginView,
    logoutView,
    dashboardView,
    uploadPhotoView,
    sharePhotoView,
    deletePhotoView,
    redirectToLogin,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", registerView, name="register"),
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),
    path("dashboard/", dashboardView, name="dashboard"),
    path("dashboard/upload/", uploadPhotoView, name="uploadPhoto"),
    path("share/", sharePhotoView, name="sharePhoto"),
    path("delete/", deletePhotoView, name="deletePhoto"),
    path("", redirectToLogin, name="redirectToLogin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)