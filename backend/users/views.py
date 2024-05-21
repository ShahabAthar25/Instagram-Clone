from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = RefreshToken.for_user(user)

        data = serializer.data
        data['tokens'] = { 'access': str(token.access_token), 'refresh': str(token) }
        
        return Response(data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)

        data = serializer.data
        data['tokens'] = { 'access': str(token.access_token), 'refresh': str(token) }
        
        return Response(data, status=status.HTTP_200_OK)
    
class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.body)
            serializer.is_valid(raise_exception=True)
            refresh_token = serializers.data["refresh"]

            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class FollowUnfollowView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, user_id, *args, **kwargs):
        try:
            follower = request.user
            followed = get_object_or_404(User, pk=user_id)

            UserFollowing.objects.create(follower=follower, followed=followed)
            followed.followers.add(follower)
            follower.following.add(followed)
            
            return Response(f"You have followed @{followed.username}.")
        except Exception as e:
            return Response("You have already followed this user.", status=status.HTTP_409_CONFLICT)
        
    def delete(self, request, user_id, *args, **kwargs):
        follower = request.user
        followed = get_object_or_404(User, pk=user_id)

        user_following = UserFollowing.objects.filter(follower=follower, followed=followed)
        if not user_following.exists():
            return Response("You have not followed this user.", status=status.HTTP_409_CONFLICT)

        user_following.delete()
        followed.followers.remove(follower)
        follower.following.remove(followed)
        
        return Response(f"You have unfollowed @{followed.username}.")