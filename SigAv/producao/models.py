from django.db import models
from datetime import date
from lote.models import Lote #importa a classe que stá sendo referênciada através da chave estrangeira


TIPODECRIACAO = [
    ('A', 'Free range'),
    ('B', '...'),
    ('C', '...'),
]

STATUS = [
    ('A', 'Ativo'),
    ('B', 'Inativo'),
]

class Fase_postura(models.Model):
    
    
    lote = models.ForeignKey(Lote, on_delete=models.RESTRICT)
    tipo_sistema = models.CharField(max_length=1, choices=TIPODECRIACAO)
    data_chegada = models.DateField(default=date.today)
    quantidade_aves_chegada = models.PositiveIntegerField()
    quantidade_aves_final = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A') # Representa a existência ou não das aves no ambiente
    observacoes = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.tipo_sistema
    
    class Meta:
        ordering = ('status','tipo_sistema',)

class Movimento_diario_postura(models.Model):
    
    fase_postura = models.ForeignKey(Fase_postura, on_delete=models.RESTRICT)
    data = models.DateField(default=date.today)
    mortalidade = models.PositiveIntegerField()
    primeira_coleta = models.PositiveIntegerField()
    segunda_coleta = models.PositiveIntegerField()
    ovos_quebrados = models.PositiveIntegerField()
    percentual_postura = models.PositiveIntegerField(null=True, blank=True) # Valor calculado automaticamente

    def __str__(self):
        return "Fase_postura: {}, Data: {}".format(str(self.fase_postura), str(self.data))
    
    class Meta:
        ordering = ('fase_postura', 'data',)