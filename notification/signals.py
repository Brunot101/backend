from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from medida_tomada.models import MedidaTomada
from alunos.models import Aluno
from .models import Notification
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=MedidaTomada)
def create_notification_on_medidatomada_creation(sender, instance, created, **kwargs):
    if created:
        try:
            denuncia = instance.denuncia_id
            matricula_aluno = denuncia.matricula
            responsaveis_aluno = Aluno.objects.get(matricula=matricula_aluno).responsaveis.all()

            for responsavel in responsaveis_aluno:
                message = f'Nova medida relacionada a um de seus dependentes foi tomada: {instance.acao}'
                Notification.objects.create(user=responsavel.user, medida_tomada=instance, message=message)
        except ObjectDoesNotExist:
            # Não faça nada se o objeto Aluno não for encontrado
            pass