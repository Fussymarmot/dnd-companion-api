from rest_framework import serializers
from .models import Characters


class CharactersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = '__all__'

class CharactersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = ('id', 'name')