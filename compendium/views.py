from rest_framework import viewsets, permissions
from .models import Races, Spells, Monsters, CharactersClass
from .serializers import (
    RaceListSerializer,
    RacesSerializer,
    SpellsListSerializer,
    SpellsSerializer,
    MonstersListSerializer,
    MonstersSerializer, CharactersClassListSerializer, CharactersClassSerializer
)

# Create your views here.
class RacesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Races.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return RaceListSerializer
        return RacesSerializer

class SpellsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Spells.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return SpellsListSerializer
        return SpellsSerializer

class MonstersViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Monsters.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return MonstersListSerializer
        return MonstersSerializer

class CharactersClassViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CharactersClass.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return CharactersClassListSerializer
        return CharactersClassSerializer