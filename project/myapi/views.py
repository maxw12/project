from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
