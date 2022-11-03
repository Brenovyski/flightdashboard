from django.shortcuts import render

from django.http import HttpResponse
from sys_voos.models import CompanhiaAerea, Voo, Partida, Chegada
from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'sys_voos/index.html')

#esboco dos urls apenas para renderizar as paginas requeridas

def crud(request):
    return render(request, 'sys_voos/crud.html')

def gera_relatorio(request):
    return render(request, 'sys_voos/gera_relatorio.html')

def atualiza_status(request):
    return render(request, 'sys_voos/atualiza_status.html')

def criar_voo(request):    
    if request.method == 'POST':
        try:
            horario_stripped = datetime.strptime(request.POST['horario_previsto'], "%H:%M %d/%m/%Y")
            companhia_instance = get_object_or_404(CompanhiaAerea, nome=request.POST['companhia'])
            voo = {
                'codigo': request.POST['codigo'],
                'companhia': companhia_instance,
                'local': request.POST['local'],
                'horario_previsto': horario_stripped,
            }

            record = Voo(**voo)
            record.save()
            context = {
                'obj': True,
                'error': False,
            }
        except ValueError:
            context = {
                'obj': False,
                'error': True, 
            }
            return render(request, 'sys_voos/criar_voo.html', context)
        except:
            context = {
                'obj': False,
                'error': True, 
            }
            return render(request, 'sys_voos/criar_voo.html', context)
    else:
        context = {
            'obj': False,
            'error': False,
        }
    return render(request, 'sys_voos/criar_voo.html', context)

def editar_voo(request): 
    return render(request, 'sys_voos/editar_voo.html')

def ler_voo(request): 
    return render(request, 'sys_voos/ler_voo.html')

def deletar_voo(request): 
    return render(request, 'sys_voos/deletar_voo.html')


