from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .tasks import send_welcome_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "Welcome to the public API!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user
    data = UserSerializer(user).data
    return Response({"message": "This is protected", "user": data})

@api_view(['GET'])
def test_email_task(request):
    send_welcome_email.delay("youremail@example.com")
    return Response({"message": "Email task triggered!"})

