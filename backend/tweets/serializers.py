from rest_framework import serializers

from .models import Tweet
from users.serializers import UserSerializer

class TweetSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = "__all__"
        extra_kwargs = {
            "created_at": { "read_only": True },
            "views": { "read_only": True },
            "id": { "read_only": True },
        }
    
    def create(self, validated_data):
        user = self.context["request"].user
        return Tweet.objects.create(owner=user, **validated_data)