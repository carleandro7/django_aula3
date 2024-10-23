from django.db import models

# Create your models here.

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