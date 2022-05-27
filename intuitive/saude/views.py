from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import *
    # Falta o upload to no models file_uploaded


def index(request):
    if request.method == 'POST':
        file_uploaded = request.FILES['file-upload']
        print(file_uploaded)
        # with open(file_uploaded, 'r') as file:
        #     csv_file = csv.reader(file, delimiter=";")
        #     for line in csv_file:
        #         print(line)
        return render(request, "saude/submit.html")
    return render(request, 'saude/submit.html')
