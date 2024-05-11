from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, max_length=20, required=True, write_only=True
    )
    password2 = serializers.CharField(
        min_length=8, max_length=20, required=True, write_only=True
    )

    class Meta:
        model = User
        fields = (
            "phone_number",
            "password",
            "password2",
            "first_name",
            "last_name",

        )

    def validate(self, attrs: dict) -> dict:
        password = attrs['password']
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Пароли не совпадают."}
            )

        validate_password(password)

        return attrs

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone number', 'email', 'first_name', 'last_name')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'is_staff')
