from django.contrib.auth import get_user_model
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from .serializers import *

User = get_user_model()

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
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)