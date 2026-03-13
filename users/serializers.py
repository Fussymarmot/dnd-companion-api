from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from characters.serializers import CharactersListSerializer

User = get_user_model()
#сериализация регистрации
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

#сериализатор для логина
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


#сериализатор своего профиля
class UserPrivateSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='profile.bio', read_only=True)
    avatar = serializers.ImageField(source='profile.image', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'avatar')


class AccountUpdateSerializer(serializers.ModelSerializer):
    # профиль
    bio = serializers.CharField(source='profile.bio', required=False, allow_blank=True)
    image = serializers.ImageField(source='profile.image', required=False)

    # новый пароль
    new_password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'old_password', 'new_password', 'bio', 'image')

    def validate(self, attrs):
        user = self.instance

        # проверяем смену пароля
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        if new_password:
            if not old_password:
                raise serializers.ValidationError({"old_password": "Old password is required to set a new password."})
            if not user.check_password(old_password):
                raise serializers.ValidationError({"old_password": "Old password is incorrect."})
            try:
                validate_password(new_password, user)
            except Exception as e:
                raise serializers.ValidationError({"new_password": list(e.messages)})

        return attrs

    def update(self, instance, validated_data):
        # обновляем username
        username = validated_data.get('username')
        if username:
            instance.username = username

        # обновляем пароль
        new_password = validated_data.get('new_password')
        if new_password:
            instance.set_password(new_password)

        instance.save()

        # обновляем профиль
        profile_data = validated_data.get('profile', {})
        profile = instance.profile
        bio = profile_data.get('bio')
        if bio is not None:
            profile.bio = bio
        image = profile_data.get('image')
        if image is not None:
            profile.image = image
        profile.save()

        return instance

#сериализатор публичных профилей
class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source="profile.bio", read_only=True)
    image = serializers.ImageField(source="profile.image", read_only=True)
    characters = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "bio", "image", "characters")

    def get_characters(self, obj):
        chars = obj.characters.all()
        return CharactersListSerializer(chars, many=True).data