"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse, request
from . import view

# import zagadjenje.view

urlpatterns = [
    path('', view.home, name='home'),
    path('admin/', admin.site.urls),
    path('kontakt',view.kontakt),
    path('photos', view.fotke),
    path('live-cameras.html', view.kamere),
    path('contact.html', view.kontakt),
    path('photos.html', view.fotke),
    path('index.html', view.home),
    path('index',view.home)
]
