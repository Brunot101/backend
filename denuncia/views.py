from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Denuncia
from .serializers import DenunciaSerializer

#Cria uma denuncia, não precisa de autenticação
class DenunciaCreateView(generics.CreateAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

#Pega a lista de denuncias, precisa de autenticação
class DenunciaListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

#Pega o id da denuncia e retorna os dados da denuncia, precisa de autenticação
class DenunciaRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer