from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.ReadOnlyField(read_only=True)
    is_superuser = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'user_type', 'is_superuser', 'email', "first_name", "last_name")


class UserPublicSerializer(serializers.ModelSerializer):
    user_type = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', "first_name", "last_name", "user_type")
