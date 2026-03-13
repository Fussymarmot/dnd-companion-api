from rest_framework import viewsets, permissions
from .models import Races, Spells, Monsters, CharactersClass
from .serializers import (
    RaceListSerializer,
    RacesDetailSerializer,
    SpellsListSerializer,
    SpellsDetailSerializer,
    MonstersListSerializer,
    MonstersDetailSerializer, CharactersClassListSerializer, CharactersClassDetailSerializer
)

# Create your views here.
class RacesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Races.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return RaceListSerializer
        return RacesDetailSerializer

class SpellsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Spells.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return SpellsListSerializer
        return SpellsDetailSerializer

class MonstersViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Monsters.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return MonstersListSerializer
        return MonstersDetailSerializer

class CharactersClassViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CharactersClass.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return CharactersClassListSerializer
        return CharactersClassDetailSerializer