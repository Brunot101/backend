from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

class UserNotificationListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        
        user_pk = self.kwargs.get('pk')

        # Obtenha o usuário com base no pk da URL
        user = get_object_or_404(User, pk=user_pk)


        # Filtrar as notificações do usuário autenticado
        queryset = Notification.objects.filter(user=user)

        return queryset
    
class UserNotificationUpdateSeenView(APIView):
    def post(self, request):
        id_value = request.data.get('id')
        try:
            notification = Notification.objects.get(id=id_value)
            notification.is_read = True
            notification.save()
            return Response(status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)