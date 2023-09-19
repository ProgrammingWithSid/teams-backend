"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from users.apis.viewsets import *
from users.views import product_views as views

from teams.apis.viewsets import *

router = DefaultRouter()
router.register("teams", TeamViewsets, basename="teams")
router.register("team-list", TeamListViewsets, basename="team-list")
router.register("players", PlayerViewsets, basename="players")
router.register("user-orders", UserOrdersViewsets, basename="orders")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("", include(router.urls)),
    
    path('auth/api/',include('users.urls')),
]
