# entries/urls.py
"""
Чтобы увидеть шаблоны в действии,
вам необходимо связать свои представления с URL-адресами .
Django работает с urls.pyфайлом для отправки входящих запросов от пользователей в браузере.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.EntryListView.as_view(),
        name="entry-list"
    ),
    path(
        # Маршрут Строка шаблона, который содержит шаблон URL
        "entry/<int:pk>",
        # Ссылка на представление , которое является as_view()функцией для представлений на основе классов.
        views.EntryDetailView.as_view(),
        name="entry-detail"
    ),
    path(
        "create",
        views.EntryCreateView.as_view(),
        name="entry-create"
    ),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
]
