from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Tweet
from .serializers import *
from .permissions import TweetReplyPermissions

class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (TweetReplyPermissions,)
    lookup_field = "pk"