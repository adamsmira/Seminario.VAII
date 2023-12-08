from django.db import models

class Aluno(models.Model):

    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    dataNascimento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class professor(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)

class turma(models.Model):
     codigo = models.CharField(max_length=100)
     codigoCurso = models.CharField(max_length=100)   
    
class curso(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    
class disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

class DetalheTurma(models.Model):
    CodigoAluno = models.CharField(max_length=100)
    CodigoProfessor = models.CharField(max_length=100)
    CodigoTurma = models.CharField(max_length=100)

class DetalheCurso(models.Model):
    codigoCurso = models.CharField(max_length=100)
    CodigoTurma = models.CharField(max_length=100)    

class DetalheDisciplina(models.Model):
    codigoCurso = models.CharField(max_length=100)
    CodigoDisciplina = models.CharField(max_length=100)

