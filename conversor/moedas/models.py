from django.db import models

class Conversao(models.Model):
    de_moeda = models.CharField(max_length=3)
    para_moeda = models.CharField(max_length=3)
    valor = models.FloatField()
    resultado = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.valor} {self.de_moeda} -> {self.para_moeda}: {self.resultado}"

#de_moeda = moeda de origem
#para moeda = moeda de destino
#valor = valor para converter
#resultado = valor convertido
#data é para registrar a data e  hora que foi convertido

#def str é para retornar uma string fomrmatada valor convertido, a moeda de origem, a moeda de destino e o resultado