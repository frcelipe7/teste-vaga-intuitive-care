from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import csv
from os import remove, path
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

            file_saved_path = f"{BASE_DIR}/saude/static/{save_file.csv_file}"

            ####  EU USEI ISSO PRA DESCOBRIR A FORMA QUE O ARQUIVO FOI CODIFICADO  ####
            # with open(f"{BASE_DIR}/saude/static/{save_file.csv_file}", 'rb') as file:
            #     print(chardet.detect(file.read()))

            ifile  = open(file_saved_path, "rt", encoding="ISO-8859-1")
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
                    dia = row[18][0:2]
                    mes = row[18][3:5]
                    ano = row[18][6:10]
                    data_registro = f'{ano}-{mes}-{dia}'
                    new_register = RegistroEmpresa(
                        registro_ans=row[0], cnpj=row[1],
                        razao_social=row[2], nome_fantasia=row[3],
                        modalidade=row[4], logradouro=row[5],
                        numero=row[6], complemento=row[7],
                        bairro=row[8], cidade=row[9],
                        uf=row[10], cep=row[11],
                        ddd=row[12], telefone=row[13],
                        fax=row[14], endereco_eletronico=row[15],
                        representante=row[16], cargo_representante=row[17],
                        data_registro_ans=data_registro,
                    )
                    new_register.save()
            ifile.close()

            delete_file = CSVFiles.objects.get(csv_file=save_file.csv_file)
            delete_file.delete()
            if path.exists(file_saved_path):
                remove(file_saved_path)

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