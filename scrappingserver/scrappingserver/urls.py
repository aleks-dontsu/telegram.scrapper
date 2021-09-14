"""scrappingserver URL Configuration

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
from scrapperapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/set_filter/', views.setUsersCollectorFilter),
    path('users/set_settings/', views.setUsersCollectorSettings),
    path('users/run/', views.runUsersCollector),
    path('users/pause/', views.pauseUsersCollector),
    path('users/unpause/', views.unpauseUsersCollector),
    path('users/stop/', views.stopUsersCollector),
    path('users/endless/', views.startEndlessUsersCollector),
    path('photos/set_filter/', views.setPhotosCollectorFilter),
    path('photos/set_settings/', views.setPhotosCollectorSettings),
    path('photos/run/', views.runPhotosCollector),
    path('photos/pause/', views.pausePhotosCollector),
    path('photos/unpause/', views.unpausePhotosCollector),
    path('photos/stop/', views.stopPhotosCollector),
    path('photos/endless/', views.startEndlessPhotosCollector),
    path('status/', views.status),
]
