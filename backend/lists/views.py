from rest_framework import generics, status
from rest_framework.response import Response
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

class FollowUnfollowListView(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        _list = get_object_or_404(List, pk=kwargs.get("pk"))

        if _list.followed_users.filter(id=request.user.id).exists():
            return Response("You have already followed this list.", status=status.HTTP_409_CONFLICT)

        _list.followed_users.add(request.user)

        return Response("You have followed this list.", status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        _list = get_object_or_404(List, pk=kwargs.get("pk"))

        if not _list.followed_users.filter(id=request.user.id).exists():
            return Response("You have not followed this list.", status=status.HTTP_400_BAD_REQUEST)

        _list.followed_users.remove(request.user)

        return Response("You have unfollowed this list.", status=status.HTTP_200_OK)