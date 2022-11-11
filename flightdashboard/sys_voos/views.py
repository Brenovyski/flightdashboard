from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.shortcuts import get_object_or_404

from sys_voos.forms import CodigoForm
from sys_voos.models import Voo
from django.core.exceptions import MultipleObjectsReturned

from sys_voos.models import CompanhiaAerea, Voo, Partida, Chegada
from django.utils import timezone
from datetime import datetime

from django.views.generic.base import TemplateView

def index(request):
    return render(request, 'sys_voos/index.html')

#esboco dos urls apenas para renderizar as paginas requeridas

def crud(request):
    return render(request, 'sys_voos/crud.html')

def gera_relatorio(request):
    return render(request, 'sys_voos/gera_relatorio.html')

class painel(TemplateView):
    template_name = "sys_voos/painel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partidas'] = Partida.objects.all()
        context['chegadas'] = Chegada.objects.all()
        print(context)
        return context

def check_status_order_partida(status_now, status_applied):
    status_order = {
        'EM': 1,
        'CA': 10, #cancelado nao pode mudar de status
        'PR': 2,
        'TA': 3,
        'PO': 4,
        'AU': 5,
        'VO': 6,
        'AT': 10, #atterisado nao existe
    }
    
    if status_order[status_now] + 1 ==  status_order[status_applied]:
        return status_applied
    else:
        return False
def atualiza_status(request):
    if request.method == 'POST':
        try:
            print(request.POST)
            voo_instance = get_object_or_404(Voo, codigo=request.POST['codigo'])
        except Exception as error:
            messages.error(request, "Código de voo inválido, tente novamente.")
            return HttpResponseRedirect('/atualiza_status')
        if request.POST['vootype'] == 'partida':
            try:
                partida_instance = get_object_or_404(Partida, voo=voo_instance)
                if check_status_order_partida(partida_instance.status, request.POST['statusform']):
                    partida_instance.status = request.POST['statusform']
                    if request.POST['statusform'] == 'VO':
                        partida_instance.horario_real = timezone.now()
                    partida_instance.save()
                    messages.success(request, "Voo atualizado com sucesso.")
                else:
                    messages.error(request, "Status inválido, tente novamente.")
            except Exception as error:
                if "No Partida matches the given query." in str(error):
                    if request.POST['statusform'] == "EM" or request.POST['statusform'] == "CA":
                        partida = {
                            'voo': voo_instance,
                            'status': request.POST['statusform'],
                            'data': timezone.now(),
                        }
                        record = Partida(**partida)
                        record.save()
                        messages.success(request, "Voo atualizado com sucesso.")
                    else:
                        messages.error(request, "Status inválido, tente novamente.")
                        return HttpResponseRedirect('/atualiza_status')
        else:
            try:
                chegada_instance = get_object_or_404(Chegada, voo=voo_instance)
                if request.POST['statusform'] == 'AT':
                    chegada_instance.status = request.POST['statusform']
                    chegada_instance.horario_real = timezone.now()
                    chegada_instance.save()
                    messages.success(request, "Voo atualizado com sucesso.")
                else:
                    messages.error(request, "Status inválido, tente novamente.")
            except Exception as error:
                if "No Chegada matches the given query." in str(error):
                    if request.POST['statusform'] == "VO":
                        chegada = {
                            'voo': voo_instance,
                            'status': request.POST['statusform'],
                            'data': timezone.now(),
                        }
                        record = Chegada(**chegada)
                        record.save()
                        messages.success(request, "Voo atualizado com sucesso.")
                    else:
                        messages.error(request, "Status inválido, tente novamente.")
                        return HttpResponseRedirect('/atualiza_status')
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
            print(error.__class__.__name__)
            if "No Voo matches the given query." in str(error):
                error = "Esse código de voo não existe."
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
    context = {}
    if request.method == 'POST':
        try:
            voo_instance = get_object_or_404(Voo, codigo=request.POST['codigo'])
            context = {
                'voo': voo_instance
            }
            return render(request, 'sys_voos/ler_voo.html', context)
        except Exception as error:
            print(error.__class__.__name__)
            print(error)
            if "No Voo matches the given query." in str(error):
                messages.error(request, "Código de voo inválido, voo não existe.")
            return render(request, 'sys_voos/ler_voo.html', context)
    else:
        return render(request, 'sys_voos/ler_voo.html', context)


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


def relatorio_chegadas(request): 
    return render(request, 'sys_voos/relatorio_chegadas.html')

def relatorio_movimentacoes(request): 
    return render(request, 'sys_voos/relatorio_movimentacoes.html')

def relatorio_partidas(request): 
    return render(request, 'sys_voos/relatorio_partidas.html')

