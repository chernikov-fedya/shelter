import django_filters

from .models import *

class AnimalFilter(django_filters.FilterSet):
    class Meta:
        model = Animal
        fields = ('type', 'breed', 'gender', 'age', 'size', 'in_shelter', 'temperament')
