"""config URL Configuration

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
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('chicken_result', chicken_result, name='chicken_result'),
    path('ilsik_result', ilsik_result, name='ilsik_result'),
    path('bunsik_result', bunsik_result, name='bunsik_result'),
    path('yasik_result', yasik_result, name='yasik_result'),
    path('jokbal_result', jokbal_result, name='jokbal_result'),
    path('jungsik_result', jungsik_result, name='jungsik_result'),
    path('jimtang_result', jimtang_result, name='jimtang_result'),
    path('cafe_result', cafe_result, name='cafe_result'),
    path('fastfood_result', fastfood_result, name='fastfood_result'),
    path('hansik_result', hansik_result, name='hansik_result'),
    path('etc_result', etc_result, name='etc_result'),
]
