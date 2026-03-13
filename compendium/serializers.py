from rest_framework import serializers
from .models import Races, Spells, Monsters, CharactersClass


class RaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Races
        fields = ('id', 'name')

class RacesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Races
        fields = '__all__'

class SpellsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spells
        fields = ('id', 'name', 'level')

class SpellsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spells
        fields = '__all__'

class MonstersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monsters
        fields = ('id', 'name')

class MonstersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monsters
        fields = '__all__'

class CharactersClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharactersClass
        fields = ('id', 'name')

class CharactersClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharactersClass
        fields = '__all__'