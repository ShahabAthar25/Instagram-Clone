from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
    
class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "profile_pic", "bio", "website", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)