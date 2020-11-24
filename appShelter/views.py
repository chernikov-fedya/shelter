from appShelter.models import *
from .utils import *
from django.db.models import Q, Sum, Count
from django.shortcuts import render, get_object_or_404
import pandas as pd
from .filters import AnimalFilter

def index(request):
    search_query = request.GET.get('search', '')#поиск_животных
    if search_query:
        all_animal = Animal.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query)|
                                           Q(age__name__icontains=search_query))
    else:
        all_animal = Animal.objects.all()
    context = {
                'all_animal': all_animal,
               }

    return render(request, "index.html", context)

def animalcard(request, slug, id):
    animal = get_object_or_404(Animal, slug=slug, id=id)
    return render(request, "animal-card.html", {'animal': animal})

def catalog(request):
    animals = Animal.objects.all()
    myFilter = AnimalFilter(request.GET, queryset=animals)
    animals = myFilter.qs
    context = {'animals': animals, 'myFilter': myFilter}
    return render(request, "catalog.html", context)
