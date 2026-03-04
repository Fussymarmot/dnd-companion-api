from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from .serializers import UserSerializer, UserPrivateSerializer, RegisterSerializer, LoginSerializer, AccountUpdateSerializer
from django.contrib.auth import get_user_model


# Create your views here.
User = get_user_model()

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]

    # регистрация
    @action(detail=False, methods=['post'], url_name='register', serializer_class=RegisterSerializer)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

    # вход
    @action(detail=False, methods=['post'], url_name='login', serializer_class=LoginSerializer)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, username=email, password=password)

        if not user:
            return Response({"detail": "Incorrect email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

class AccountViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    #приватный пользователь
    @action(detail=False, methods=['get'], url_name='me')
    def me(self, request):
        serializer = UserPrivateSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    #обновление инфы об аккаунте
    @action(detail=False, methods=['patch'], url_name='update_account', serializer_class=AccountUpdateSerializer)
    def update_account(self, request):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "Account updated successfully.",
            "user": serializer.data
        }, status=status.HTTP_200_OK)

#профиль пользователя по нику
class UserProfileRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "username"

