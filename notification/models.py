from django.db import models
from django.contrib.auth.models import User
from medida_tomada.models import MedidaTomada

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    medida_tomada = models.ForeignKey(MedidaTomada, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Usuário: {self.user}, Mensagem: {self.message}"