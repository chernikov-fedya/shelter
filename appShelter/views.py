from random import Random
from django.shortcuts import render, get_object_or_404
from appShelter.models import Animal


def index(request):
    all_animal = Animal.objects.all()
    context = {'all_animal': all_animal}
    return render(request, "index.html", context)

def animalcard(request, slug, id):
    animal = get_object_or_404(Animal, slug=slug, id=id)
    return render(request, "animal-card.html", {'animal': animal})

def catalog(request):
    return render(request, "catalog.html", )
