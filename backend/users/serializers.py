from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField("get_followers")
    following = serializers.SerializerMethodField("get_following")
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "profile_pic", "bio", "website", "followers", "following")
    
    def get_followers(self, obj):
        return obj.followers.count()
    
    def get_following(self, obj):
        return obj.following.count()

class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "profile_pic", "bio", "website", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()