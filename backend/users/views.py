from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *

User = get_user_model()

class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = RefreshToken.for_user(user)

        data = serializer.data
        data['tokens'] = { 'access_token': str(token.access_token), 'refresh_token': str(token) }
        
        return Response(data, status=status.HTTP_201_CREATED)
    