from django.db import models

# Create your models here.
class registro_empresa(models.Model):
    registro_ans = models.CharField(blank=False, default='123456', max_length=6)
    cnpj = models.CharField(blank=False, default='11223334444555', max_length=15)
    razao_social = models.CharField(blank=False, default='razao_social', max_length=100)
    nome_fantasia = models.CharField(blank=False, default='nome_fantasia', max_length=100)
    modalidade = models.CharField(blank=False, default='modalidae', max_length=100)
    logradouro = models.CharField(blank=False, default='logradouro', max_length=100)
    numero = models.CharField(blank=False, default='numero', max_length=100)
    complemento = models.CharField(blank=False, default='complemento', max_length=100)
    bairro = models.CharField(blank=False, default='bairro', max_length=100)
    cidade = models.CharField(blank=False, default='cidade', max_length=100)
    uf = models.CharField(blank=False, default='uf', max_length=100)
    cep = models.CharField(blank=False, default='cep', max_length=100)
    ddd = models.CharField(blank=False, default='ddd', max_length=100)
    telefone = models.CharField(blank=False, default='telefone', max_length=100)
    fax = models.CharField(blank=False, default='fax', max_length=100)
    endereco_eletronico = models.CharField(blank=False, default='endereco_eletronico', max_length=100)
    representante = models.CharField(blank=False, default='representante', max_length=100)
    cargo_representante = models.CharField(blank=False, default='cargo_representante', max_length=100)
    data_registro_ans = models.DateField(default="1/1/2001", blank=False)


class file_uploaded(models.Model):
    # (serve pra salvar o arquivo antes da leitura)
    file = models.FileField()
    # Falta o upload to