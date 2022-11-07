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
from django.core.exceptions import MultipleObjectsReturned

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
            try:
                get_object_or_404(Voo, codigo=request.POST['codigo'])
                raise MultipleObjectsReturned
            except MultipleObjectsReturned as error:
                print(error)
                context = {
                    'obj': False,
                    'error': str(error) + "Codigo já existe. Digite um novo.", 
                }
                return render(request, 'sys_voos/criar_voo.html', context)
            except Exception as error:
                a = True
                print(error.__class__.__name__)
                if "No Voo matches the given query." in str(error):
                    a = False
                context = {
                    'obj': False,
                    'error': error, 
                }
                if a:
                    return render(request, 'sys_voos/criar_voo.html', context)
            horario_stripped = datetime.strptime(request.POST['horario_previsto'], "%H:%M")
            companhia_instance = get_object_or_404(CompanhiaAerea, nome=request.POST['companhia'])
            voo = {
                'codigo': request.POST['codigo'],
                'companhia': companhia_instance,
                'local': request.POST['local'],
                'horario_previsto': horario_stripped,
            }

            record = Voo(**voo)
            record.save()
            print(voo)
            context = {
                'obj': True,
                'error': False,
            }
        except Exception as error:
            if "No CompanhiaAerea matches the given query." in str(error):
                error = "Essa companhia aérea não existe."
            context = {
                'obj': False,
                'error': error, 
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
    if request.method == 'POST':
        try:
            voo_instance = get_object_or_404(Voo, codigo=request.POST['codigo'])
            if request.POST['companhia'] != '':
                companhia_instance = get_object_or_404(CompanhiaAerea, nome=request.POST['companhia'])
                voo_instance.companhia = companhia_instance
            if request.POST['local'] != '':
                voo_instance.local = request.POST['local']
            if request.POST['horario_previsto'] != '':
                horario_stripped = datetime.strptime(request.POST['horario_previsto'], "%H:%M")
                voo_instance.horario_previsto = horario_stripped
            voo_instance.save()
            context = {
                'obj': True,
                'error': False,
            }
        except Exception as error:
            if "No CompanhiaAerea matches the given query." in str(error):
                error = "Essa companhia aérea não existe."
            context = {
                'obj': False,
                'error': error, 
            }
            return render(request, 'sys_voos/editar_voo.html', context)
    else:
        context = {
            'obj': False,
            'error': False,
        }
    return render(request, 'sys_voos/editar_voo.html', context)


def ler_voo(request): 
    return render(request, 'sys_voos/ler_voo.html')


def deletar_voo(request):
    if request.method == 'POST':
        form = CodigoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            voo = Voo.objects.filter(codigo=codigo)
            if not voo:
                messages.error(request, "Código de voo inválido, voo não deletado.")
            else:
                voo.delete()
                messages.success(request, "Voo deletado com sucesso.")
            return HttpResponseRedirect('/deletar_voo')
    else:
        return render(request, 'sys_voos/deletar_voo.html')





