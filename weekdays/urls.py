from django.urls import path

from .views import uz, weekdays, en, ru

urlpatterns = [
    path('weekdays/', weekdays, name='weekdays_url'),
    path('weekdays/uz/', uz, name='uz_url'),
    path('weekdays/en/', en, name='en_url'),
    path('weekdays/ru/', ru, name='ru_url'),
]