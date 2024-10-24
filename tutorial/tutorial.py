entre dentro da pasta que deseja criar o projeto
passo 1: cria o projeto. Exemplo de nome sistema
django-admin startproject sistema

passo 2: entra na pasta no projeto
cd sistema

passo 3: abre o vscode
code .

passo 4: cria uma aplicação: exemplo vendas. Troque para o nome que deseja
python manage.py startapp vendas
passo 5: adicione o nome da aplicação ao projeto

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vendas', #nome da aplicação criada
]

passo 6: adicione na urls.py a seguinte linha do projeto
path('vendas/', include('vendas.urls')),
*no import altere a linha adicionado o include
from django.urls import path, include

passo 7: adicione linguagem do site (PT-BR) e o caminho do template. substitua no final do arquivo de settings.py
LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

#pasta do template
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
import os #coloque no inicio do arquivo

altere tambem a linha abaixo:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #essa linha
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


passo 8: crie as pasta 
*templates dentro da pasta do projeto.
* dentro de templates crie a pasta static e o arquivo base.html
* dentro de static: css, js e img
* dentro de css crie o arquivo base.css
* dentro de js crie o arquivo base.js

passo 9: coloque os dados de base.html. Olhe cada parte do html
passo 10: coloque o css. veja cada detalhe do css

em vendas: 
passo 11: no models.py crie o modelos:
class Aluno(models.Model):
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=11, unique=True) 
    matricula = models.CharField(max_length=15, unique=True) 

    def __str__(self): 
        return self.nome

class Ficha(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)  
    data_compra = models.CharField(max_length=100) 
    valor = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self): 
        return f"{self.data_compra} - {self.valor}"

passo 12: em admin.py adicione os modelos criados
from django.contrib import admin
from .models import Aluno, Ficha

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Ficha)

passo 13: crie os arquivos forms.py e urls.py
passo 14: em forms.py adicione os fomurlarios dos modelos
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


#comando no terminal
python manage.py makemigrations
python manage.py migrate

passo 15: adicione as urls para iniciar a criação das paginas:
obs: vamos liberando as funções na url a medida que forem criando na views.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    #path('novo/', views.criar_aluno, name='criar_aluno'),
    #path('editar/<int:id>/', views.atualizar_aluno, name='atualizar_aluno'),
    #path('deletar/<int:id>/', views.deletar_aluno, name='deletar_aluno'),

    #path('fichas', views.listar_fichas, name='listar_fichas'),
    #path('fichas/novo/', views.criar_ficha, name='criar_ficha'),
    #path('fichas/editar/<int:id>/', views.atualizar_ficha, name='atualizar_ficha'),
    #path('fichas/deletar/<int:id>/', views.deletar_ficha, name='deletar_ficha'),
]

passo 16: criar a função na views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

passo 17: criar a pasta templates e dentro a pasta alunos.
passo 18: criar o arquivo: lista_alunos.html
passo 19: adicionar o conteudo do arquivo lista_alunos.html

passo 20: liberar na urls.py o novo, para criar aluno e adicionar o codigo abaixo na views.py
def criar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/criar_aluno.html', {'form': form})

passo 21: criar o arquivo criar_aluno.html dentro da pasta alunos.

passo 22: adicionar o conteudo do arquivo criar_aluno.html

passo 23: adicionar a url de criar_aluno.html em listar_aluno.html
<a href="{% url 'criar_aluno' %}" class="btn colorprimarybtn2 mb-3">Adicionar aluno</a>

passo 24: liberar na urls o editar, para poder editar o aluno e adicionar o codigo abaixo em views.py

def atualizar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/atualizar_aluno.html', {'form': form})

passo 25: adicionar o conteudo do arquivo atualizar_aluno.html
passo 26: adicionar a url de atualizar_aluno.html em listar_aluno.html
<a href="{% url 'atualizar_aluno' aluno.id %}" class="btn btn-sm btn-warning">Editar</a>

passo 27: liberar na urls o deletar, para poder editar o aluno e adicionar o codigo abaixo em views.py
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        aluno.delete()
        return redirect('listar_alunos')  # Redireciona para a lista de alunos
    return render(request, 'alunos/deletar_aluno.html', {'aluno': aluno})

passo 28: em listar_aluno.html altere o codigo para ficar assim em deltear aluno
<form action="{% url 'deletar_aluno' aluno.id %}" method="POST" style="display:inline;">



para adicionar uma imagem: 
1. coloque a imagem dentro da pasta /templates/img
2. e no html coloque
<img src="{% static 'img/nome_da_imagem.extensao' %}">

