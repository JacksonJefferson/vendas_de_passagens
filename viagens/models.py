from django.db import models

class Passagem(models.Model):
    origem = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    poltrona = models.IntegerField()
    valor = models.DecimalField(max_digits=9,decimal_places=2)
    data = models.DateField()

class Veiculo(models.Model):
    categoria = models.CharField(max_length=50)
    chassi = models.CharField(max_length=50)
    qtd_pessoas = models.IntegerField()
    km_rodados = models.IntegerField()
    leito = models.BooleanField()

