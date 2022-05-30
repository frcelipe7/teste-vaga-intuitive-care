from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import csv
import io
from intuitive.settings import BASE_DIR

from .models import *
from .form import *

####  EU USEI ISSO PRA DESCOBRIR A FORMA QUE O ARQUIVO FOI CODIFICADO  ####
# import chardet


# Tem q faze o upload e leitura do arquivo CSV 
def index(request):
    if request.method == 'POST':
        form = FormCsv(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['input_csv']
            save_file = CSVFiles(csv_file=file)
            save_file.save()

            ####  EU USEI ISSO PRA DESCOBRIR A FORMA QUE O ARQUIVO FOI CODIFICADO  ####
            # with open(f"{BASE_DIR}/saude/static/{save_file.csv_file}", 'rb') as file:
            #     print(chardet.detect(file.read()))

            print(save_file.csv_file)
            ifile  = open(f"{BASE_DIR}/saude/static/{save_file.csv_file}", "rt", encoding="ISO-8859-1")
            read = csv.reader(ifile, delimiter=";")
            for row in read:
                rows_to_ignore = [
                    ['Relação de Operadoras Ativas ANS'],
                    [],
                    ['Registro ANS', 'CNPJ', 'Razão Social', 'Nome Fantasia',
                    'Modalidade','Logradouro', 'Número', 'Complemento', 'Bairro',
                    'Cidade', 'UF', 'CEP', 'DDD', 'Telefone', 'Fax', 'Endereço eletrônico',
                    'Representante', 'Cargo Representante', 'Data Registro ANS']
                ]
                if row not in rows_to_ignore:
                    print(f'Registro ANS: {row[0]}, CNPJ: {row[1]}, Razão Social: {row[2]}, Nome Fantasia: {row[3]}')

        return render(request, "saude/submit.html", {
            'form': FormCsv
        })
    return render(request, 'saude/submit.html', {
        'form': FormCsv
    })



'''
def addreport(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.reader(form.cleaned_data['file'])
            for row in reader:
                print row
        else:
            print form.errors
            print request.FILES
            #form = UploadFileForm()
    else:
        form = UploadFileForm()

    return render(request, 'products/addreport.html', {'form': form})
'''

def api(request):
    all_registros = RegistroEmpresa.objects.all()
    return JsonResponse(
        [registro.serialize() for registro in all_registros],
        safe=False
    )