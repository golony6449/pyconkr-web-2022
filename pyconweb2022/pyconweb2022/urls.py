"""pyconweb2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

import pyconemailer.routers
import sponsor.routers
import program.routers

urlpatterns = [
    path("admin/", admin.site.urls),
    # DRF
    path("api-auth/", include("rest_framework.urls")),
    # App
    path("sponsor/", include(sponsor.routers.get_router().urls)),
    path("news/", include("news.urls")),
    path("program/", include(program.routers.get_router().urls)),
    # PyConEmailer
    path("pyconemailer/", include("pyconemailer.urls")),
    path("api/pyconmailer/", include(pyconemailer.routers.get_router().urls)),
    # martor
    path("martor/", include("martor.urls")),
]
