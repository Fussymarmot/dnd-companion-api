from rest_framework import viewsets, permissions, status
from .serializers import CharactersDetailSerializer, CharactersListSerializer
from .models import Characters
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "You must be logged in to see your characters."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        if self.action == "list":
            if not self.request.user.is_authenticated:
                return Response({
                    "detail": "You must be logged in to see your characters.",
                }, status=status.HTTP_401_UNAUTHORIZED)
            return Characters.objects.filter(author=self.request.user)
        return Characters.objects.all()

    def get_serializer_class(self):

        if self.action == "list":
            return CharactersListSerializer

        if self.action == "retrieve":
            return CharactersDetailSerializer

        return CharactersDetailSerializer

