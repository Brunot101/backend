from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from medida_tomada.models import MedidaTomada
from alunos.models import Aluno
from denuncia.models import Denuncia
from .models import Notification
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=MedidaTomada)
def create_notification_on_medidatomada_creation(sender, instance, created, **kwargs):
    if created:
        denuncia = instance.denuncia_id
        responsaveis = set()

        # Adicione os responsáveis dos alunos envolvidos na denúncia aos responsáveis
        responsaveis.update(denuncia.vitimas.all().values_list('responsaveis__user', flat=True))
        responsaveis.update(denuncia.praticantes.all().values_list('responsaveis__user', flat=True))
        users = User.objects.filter(id__in=responsaveis)
        # Crie uma notificação para cada responsável
        for user in users:
            message = f'Nova medida tomada para a denúncia "{denuncia.titulo}": {instance.acao}'
            Notification.objects.create(user=user, medida_tomada=instance, message=message)

@receiver(m2m_changed, sender=Denuncia.vitimas.through)
@receiver(m2m_changed, sender=Denuncia.praticantes.through)
def create_notification_on_denuncia_association_change(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        responsaveis = set()

        # Obter os responsáveis dos alunos recém-adicionados
        for aluno_id in pk_set:
            aluno = model.objects.get(id=aluno_id)
            responsaveis.update(aluno.responsaveis.all())

        # Criar uma notificação para cada responsável dos novos alunos adicionados
        for responsavel in responsaveis:
            message = f'Um dependente seu está envolvido em uma nova denúncia: {instance.titulo}'
            Notification.objects.create(user=responsavel.user, denuncia=instance, message=message)