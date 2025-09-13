from django.db import models

# Create your models here.

class Universidade(Model.models):
  nome = models.CharField(max_length=70)

class Disciplina(Model.models):
  nome = models.CharField(max_length=70)
  id_universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
  
class Exame(Model.models):
  ano = models.IntegerField()
  id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
  
