from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('novo/', views.criar_aluno, name='criar_aluno'),
    path('editar/<int:id>/', views.atualizar_aluno, name='atualizar_aluno'),
    path('deletar/<int:id>/', views.deletar_aluno, name='deletar_aluno'),

    #path('fichas', views.listar_fichas, name='listar_fichas'),
    #path('fichas/novo/', views.criar_ficha, name='criar_ficha'),
    #path('fichas/editar/<int:id>/', views.atualizar_ficha, name='atualizar_ficha'),
    #path('fichas/deletar/<int:id>/', views.deletar_ficha, name='deletar_ficha'),
]