from django.contrib import admin
from .models import CompanhiaAerea, Voo, Partida, Chegada

# Register your models here.
admin.site.register(CompanhiaAerea)
admin.site.register(Voo)
admin.site.register(Partida)
admin.site.register(Chegada)