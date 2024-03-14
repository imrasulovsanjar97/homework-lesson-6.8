from django.urls import path

from .views import months

urlpatterns = [
    path('', months, name='months')
]