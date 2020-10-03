from random import Random

from django.shortcuts import render


# Create your views here.
from appShelter.models import Animal


def index(request):
    return render(request, "index.html")

def modelindex(request):
    animal: Animal = instanceAnimal()
    dict = {"animal" : animal}
    return render(request, "ModelIndex.html", dict)

def instanceAnimal():

    animal = Animal()
    animal.name = ["Кто", "ЗДЕСЬ", "Ответьте!"][Random().randint(0, 2)]
    return animal