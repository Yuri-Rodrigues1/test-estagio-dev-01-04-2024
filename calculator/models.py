from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    consumo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    cobertura = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)
    economia_anual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    economia_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class RegraDesconto(models.Model):
    tipo_consumidor = models.CharField(max_length=50)
    consumo_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    cobertura = models.DecimalField(max_digits=5, decimal_places=2)    




    #  create the foreign key for discount rule model here


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
