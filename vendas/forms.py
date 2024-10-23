from django import forms
from .models import Aluno
from .models import Ficha

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'matricula']
    


class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['data_compra', 'valor', 'aluno']