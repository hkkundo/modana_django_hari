from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
