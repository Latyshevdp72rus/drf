from rest_framework import serializers
from apps.acount.models import User


class RegistrationUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(

    )
    username =serializers.CharField(

    )
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

