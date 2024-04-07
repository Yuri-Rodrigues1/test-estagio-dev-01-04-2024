from django.shortcuts import render
from calculator_python import calculator
from calculator.models import Pessoa, RegraDesconto

# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    # Create the first view here.
    pass


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass


def listar_consumidores_economia(request):
  
    consumidores = Pessoa.objects.all()

    for consumidor in consumidores:
     
        consumo_medio = consumidor.consumo

        tipo_tarifa = consumidor.tipo

        regra_desconto = RegraDesconto.objects.filter(tipo_consumidor=tipo_tarifa, consumo_minimo__lte=consumo_medio, consumo_maximo__gte=consumo_medio).first()

 
        if regra_desconto:
            desconto = regra_desconto.desconto
            cobertura = regra_desconto.cobertura
            economia_anual = consumo_medio * (1 - desconto) * consumidor.tarifa * 12
            economia_mensal = economia_anual / 12

       
            consumidor.economia_anual = economia_anual
            consumidor.economia_mensal = economia_mensal
            consumidor.desconto = desconto
            consumidor.cobertura = cobertura
            consumidor.save()

    consumidores = Pessoa.objects.all()

    return render(request, 'listar_consumidores.html', {'consumidores': consumidores})

def index(request):
    return render(request, 'calculator/index.html')


def calcularConsumo(request):
    if request.method == 'POST':
        consumo1 = float(request.POST.get('consumo1', 0))
        consumo2 = float(request.POST.get('consumo2', 0))
        consumo3 = float(request.POST.get('consumo3', 0))
        tarifa = float(request.POST.get('tarifa', 0))
        tipoTarifa = request.POST.get('tipo', '')  

        result = calculator([consumo1, consumo2, consumo3], tarifa, tipoTarifa)

        return render(request, 'calculator/index.html', {
            'result': result,
            'economia_anual': result[0],  
            'economia_mensal': result[1], 
            'desconto_aplicado': result[2], 
            'cobertura': result[3], 
        })

    return render(request, 'calculator/index.html')