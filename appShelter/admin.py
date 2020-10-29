from django.contrib import admin
from .models import *

admin.site.register(Gender)
admin.site.register(Breed)
admin.site.register(Type)
admin.site.register(Rewies)
admin.site.register(Size)
admin.site.register(Age)
admin.site.register(Temperament)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
