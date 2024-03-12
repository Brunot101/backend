from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ResponsavelProfile
from .serializers import UserAndProfileSerializer, ResponsavelProfileSerializer
from rest_framework.permissions import IsAuthenticated
from alunos.models import Aluno


#Cria uma conta e perfil de responsável
class ResponsavelProfileCreateView(generics.CreateAPIView):
    queryset = ResponsavelProfile.objects.all()
    serializer_class = UserAndProfileSerializer

class ResponsavelProfileRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResponsavelProfile.objects.all()
    serializer_class = ResponsavelProfileSerializer

class AssociateDependenteView(APIView):
    
    def patch(self, request, *args, **kwargs):
        user_profile = request.user.responsavelprofile  # Obtém o perfil do usuário logado
        aluno_id = kwargs.get('pk')  # Obtém o ID do aluno da URL

        try:
            aluno = Aluno.objects.get(pk=aluno_id)  # Obtém o objeto Aluno com base no ID
        except Aluno.DoesNotExist:
            return Response({'error': 'Aluno not found'}, status=status.HTTP_404_NOT_FOUND)

        user_profile.dependentes.add(aluno)  # Adiciona o aluno aos dependentes do perfil do usuário

        serializer = ResponsavelProfileSerializer(user_profile)
        return Response(serializer.data)




