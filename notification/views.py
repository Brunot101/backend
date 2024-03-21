from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics

class UserNotificationListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        
        user_pk = self.kwargs.get('pk')

        # Obtenha o usuário com base no pk da URL
        user = get_object_or_404(User, pk=user_pk)


        # Filtrar as notificações do usuário autenticado
        queryset = Notification.objects.filter(user=user)

        return queryset