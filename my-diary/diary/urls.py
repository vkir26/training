"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

    Когда вы откроете diary/urls.py, вы увидите, что urlpatterns ваш проект Django Diary использует.
    Пока что есть только маршрут "admin/", который добавлен по умолчанию,
    чтобы вы могли попасть на сайт администратора Django.
    Чтобы отображать записи вашего дневника при посещении http://localhost:8000,
    вам сначала необходимо отправить корневой URL-адрес в entries приложение
"""
# diary/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("entries.urls")),
]
