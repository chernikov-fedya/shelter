from random import Random
from django.shortcuts import render
from appShelter.models import Animal


def index(request):
    return render(request, "index.html")

def animalcard(request):
    animal = Animal.objects.all()
    dict = {"animal": animal[0]}
    return render(request, "../static/animal-card.html", dict)