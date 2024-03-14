from django.urls import path

from .views import ball, pupils

urlpatterns = [
    path('', pupils, name='pupils'),
    path('ball/', ball, name = 'ball'),
]