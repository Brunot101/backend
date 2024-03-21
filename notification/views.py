from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics

class UserNotificationListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Obtenha o usuário autenticado
        user = self.request.user

        # Filtrar as notificações do usuário autenticado
        queryset = Notification.objects.filter(user=user)

        return queryset