from rest_framework import serializers
from apps.acount.models import User


class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

