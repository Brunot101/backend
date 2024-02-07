from django.db import models


CHOICES = (
        ('yes', 'Sim'),
        ('no', 'Não'),
    )

class Denuncia(models.Model):
    
    matricula = models.IntegerField()    
    relato = models.CharField(max_length = 500)
    lugar = models.CharField(max_length = 50)
    v_fisica = models.CharField(max_length = 10, choices=CHOICES)
    v_verbal = models.CharField(max_length = 10, choices=CHOICES)
    bullying = models.CharField(max_length = 10, choices=CHOICES)
    assedio =  models.CharField(max_length = 10, choices=CHOICES)
    recorrencia = models.CharField(max_length = 50)
    data_ocorrido = models.DateTimeField()
    
    v_domestica = models.CharField(max_length = 10, choices=CHOICES)
    telefone_1 = models.CharField(max_length = 15, blank=True, null=True)
    telefone_1 = models.CharField(max_length = 15, blank=True, null=True)

    data_denuncia = models.DateTimeField(auto_now_add=True)
