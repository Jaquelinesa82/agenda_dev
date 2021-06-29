from django.contrib import admin
from core.models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_evento', 'data_criacao')
    list_filter = ('usuario',)


admin.site.register(Evento, EventoAdmin)
