from django import forms

class CodigoForm(forms.Form):
    codigo = forms.CharField(label='Código de voo', max_length=10)