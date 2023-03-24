from django.contrib import admin
from .models import Entry

# Register your models here.
"""
Зарегистрируйте модель входа
Чтобы также увидеть "Entry" модель на сайте администратора Django, 
вам необходимо зарегистрировать ее в entries/admin.py
"""

admin.site.register(Entry) # - Регистрация

"""
Django не выдаст ошибку, если вы забудете зарегистрировать модель на сайте администратора. 
В конце концов, не каждой моделью нужно управлять в пользовательском интерфейсе. 
Но для минимально жизнеспособного продукта вашего дневника 
вы воспользуетесь преимуществами встроенного сайта администратора Django.
"""
