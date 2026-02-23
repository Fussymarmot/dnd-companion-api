from django.contrib import admin
from .models import Spells, CharactersClass, Races, Monsters
# Register your models here.
admin.site.register(Spells)
admin.site.register(CharactersClass)
admin.site.register(Races)
admin.site.register(Monsters)