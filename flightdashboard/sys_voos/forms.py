from django import forms

class CodigoForm(forms.Form):
    codigo = forms.CharField(label='Código de voo', max_length=10)

class FilterForm(forms.Form):
    data_inicio = forms.DateField(label='Data de início do relatório')
    data_fim = forms.DateField(label='Data de fim do relatório')
    status = forms.CharField(label='Status')
