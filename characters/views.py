from rest_framework import viewsets, permissions, generics
from .serializers import CharactersDetailSerializer, CharactersListSerializer
from .models import Characters
from .permissions import IsOwnerOrReadOnly

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.action == "list":
            return Characters.objects.filter(author=self.request.user)
        return Characters.objects.all()

    def get_serializer_class(self):

        if self.action == "list":
            return CharactersListSerializer

        if self.action == "retrieve":
            return CharactersDetailSerializer

        return CharactersDetailSerializer