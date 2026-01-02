from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class HomeView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'Message': "Welcome to the home Page"})


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        #get email and password from request data
        email = request.data.get('email')
        password = request.data.get('password')

        # validate request data 
        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response(
                {"error": "Invalid Credentials."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Generate a JWT token for the authenticated user
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Login Successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
            }
        })
