from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from sys_voos.models import CompanhiaAerea, Voo, Partida, Chegada
from datetime import datetime

from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.shortcuts import get_object_or_404

from sys_voos.forms import CodigoForm
from sys_voos.models import Voo


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
            print(voo)
            record = Voo(**voo)
            record.save()
            context = {
                'obj': True,
                'error': False,
            }
            messages.success(request, 'Voo criado com sucesso')
        except ValueError:
            context = {
                'obj': False,
                'error': True, 
            }
            # messages.warning(request, "Voo não foi criado com sucesso, verifique a formatação dos dados.")
            return render(request, 'sys_voos/criar_voo.html', context)
        except:
            context = {
                'obj': False,
                'error': True, 
            }
            messages.warning(request, "Voo não foi criado com sucesso, verifique a formatação dos dados.")
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
    if request.method == 'POST':
        form = CodigoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            voo = Voo.objects.filter(codigo=codigo)
            voo.delete()
            return HttpResponseRedirect('/deletar_voo')
    else:
        form = CodigoForm() 
        return render(request, 'sys_voos/deletar_voo.html', {'form': form})





