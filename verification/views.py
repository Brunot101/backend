from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Verification
from .serializers import VerificationSerializer, VerificationSerializerCheck

from rest_framework.response import Response


class VerificationCreateView(generics.CreateAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer

    def generate_15_digit_code(self):
        
        import random
        return ''.join(random.choices('0123456789', k=15))

    def perform_create(self, serializer):
        
        telefone = self.request.data.get('telefone')
        codigo = self.generate_15_digit_code()
        serializer.save(telefone=telefone, codigo=codigo)

    
class VerificationCheckView(generics.CreateAPIView):
    serializer_class = VerificationSerializerCheck

    def create(self, request, *args, **kwargs):
       
        codigo = request.data.get('codigo')

        
        try:
            verification_obj = Verification.objects.get(codigo=codigo)
            verification_obj.delete()
            return Response({'message': 'Código válido.'}, status=status.HTTP_200_OK)
        except Verification.DoesNotExist:
            return Response({'message': 'Código inválido.'}, status=status.HTTP_400_BAD_REQUEST)
