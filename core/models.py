from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    local = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data da Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'


    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%Mhs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        return self.data_evento < datetime.now()

    def get_evento_que_falta_menos_de_1h(self):
        return datetime.now() > self.data_evento - timedelta(hours=1) and datetime.now() < self.data_evento

