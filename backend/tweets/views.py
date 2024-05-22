from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Tweet, Reply
from .serializers import *
from .permissions import TweetReplyPermissions

class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (TweetReplyPermissions,)
    lookup_field = "pk"
    
    def list(self, request, *args, **kwargs):
        tweets = self.get_queryset()

        for tweet in tweets:
            tweet.views += 1
            tweet.save()

        queryset = self.filter_queryset(tweets)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data

            return self.get_paginated_response(data)
        
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        instance =  self.get_object()
        
        instance.views += 1
        instance.save()
        
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        return Response(data, status=status.HTTP_200_OK)