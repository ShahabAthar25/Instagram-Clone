from rest_framework import generics

from .models import List
from .serializers import ListSerializer
from tweets.permissions import IsOwnerOrReadonly

class ListCreateListsView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsOwnerOrReadonly,)
    lookup_field = "pk"