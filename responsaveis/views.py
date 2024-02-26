from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import ResponsavelProfile
from .serializers import UserAndProfileSerializer



#Cria uma conta e perfil de responsável
class ResponsavelProfileCreateView(generics.CreateAPIView):
    queryset = ResponsavelProfile.objects.all()
    serializer_class = UserAndProfileSerializer
        



