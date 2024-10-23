from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

# Create your views here.


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})


def criar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/criar_aluno.html', {'form': form})


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


def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        aluno.delete()
        return redirect('listar_alunos')  # Redireciona para a lista de alunos
    return render(request, 'alunos/deletar_aluno.html', {'aluno': aluno})

