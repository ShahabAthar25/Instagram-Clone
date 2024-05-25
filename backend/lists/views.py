from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import List
from .serializers import ListSerializer
from tweets.permissions import IsOwnerOrReadonly
from users.serializers import UserSerializer

class ListCreateListsView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsOwnerOrReadonly,)
    lookup_field = "pk"

class FollowingListUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        _list = get_object_or_404(List, id=self.kwargs["pk"])
        return _list.following_users.all()

class FollowedListUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        _list = get_object_or_404(List, id=self.kwargs["pk"])
        return _list.followed_users.all()