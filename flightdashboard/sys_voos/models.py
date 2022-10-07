from django.db import models

class CompanhiaAerea(models.Model) :
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    codigo = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'companhia_aerea'

class Voo(models.Model) :
    id = models.IntegerField(primary_key=True)
    companhia = models.ForeignKey(CompanhiaAerea, on_delete=models.CASCADE)
    horario_previsto = models.TimeField(auto_now=False, auto_now_add=False)
    local = models.CharField(max_length=200, null=False)
    
    class Meta:
        db_table = 'voo'

class Partida(models.Model) :
    departure_status_choices = [
        ('EM', 'Embarcando'),
        ('CA', 'Cancelado'),
        ('PR', 'Embarcando'),
        ('TA', 'Taxeando'),
        ('PO', 'Pronto'),
        ('AU', 'Autorizado'),
        ('VO', 'Em voo'),
    ]
    id = models.IntegerField(primary_key=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    horario = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=2, choices=departure_status_choices, default='EM')
    data = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'partida'

class Chegada(models.Model) :
    arrive_status_choices = [
        ('VO', 'Em voo'),
        ('AT', 'Aterrisado'),
    ]

    id = models.IntegerField(primary_key=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    horario = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=2, choices=arrive_status_choices, default='VO')
    data = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'chegada'
