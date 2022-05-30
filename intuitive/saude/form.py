from django import forms

class FormCsv(forms.Form):
    input_csv = forms.FileField(label="Escolha o arquivo CSV",)