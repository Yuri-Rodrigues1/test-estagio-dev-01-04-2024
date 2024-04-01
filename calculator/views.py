from django.shortcuts import render
from calculator_python import calculator


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



def index(request):
    return render(request, 'calculator/index.html')


def calcularConsumo(request):
    if request.method == 'POST':
        consumo1 = float(request.POST.get('consumo1', 0))
        consumo2 = float(request.POST.get('consumo2', 0))
        consumo3 = float(request.POST.get('consumo3', 0))
        tarifa = float(request.POST.get('tarifa', 0))
        tipoTarifa = request.POST.get('tipo', '')  # Aqui está a correção

        result = calculator([consumo1, consumo2, consumo3], tarifa, tipoTarifa)

        return render(request, 'calculator/index.html', {
            'result': result,
            'economia_anual': result[0],  # Economia Anual
            'economia_mensal': result[1],  # Economia Mensal
            'desconto_aplicado': result[2],  # Desconto Aplicado
            'cobertura': result[3],  # Cobertura
        })

    return render(request, 'calculator/index.html')