from django.db import models


CHOICES = (
        ('yes', 'Sim'),
        ('no', 'Não'),
    )

class Denuncia(models.Model):
        
    relato = models.CharField(max_length = 500)
    lugar = models.CharField(max_length = 50)
    v_fisica = models.CharField(max_length = 10, choices=CHOICES)
    v_verbal = models.CharField(max_length = 10, choices=CHOICES)
    bullying = models.CharField(max_length = 10, choices=CHOICES)
    assedio =  models.CharField(max_length = 10, choices=CHOICES)
    recorrencia = models.CharField(max_length = 50)
    data_ocorrido = models.DateTimeField()
    

