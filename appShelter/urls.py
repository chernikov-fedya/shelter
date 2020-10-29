from django.urls import path, include
from .views import *

app_name = 'appShelter'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/<slug:slug>/animalcard/', animalcard, name='animalcard'),
    path('catalog/', catalog, name='catalog'),
]
