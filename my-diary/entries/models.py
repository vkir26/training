from django.db import models
from django.utils import timezone

# Create your models here.

# entries/models.py

from django.db import models
from django.utils import timezone


class Entry(models.Model): # Entry - Модель класса
    title = models.CharField(max_length=200) # - Заголовок
    content = models.TextField() # - Основной текст
    date_created = models.DateTimeField(default=timezone.now) # - Дата и время создания

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Записи"
