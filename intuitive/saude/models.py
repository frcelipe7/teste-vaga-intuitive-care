from django.db import models

# Create your models here.
class RegistroEmpresa(models.Model):
    registro_ans = models.CharField(blank=False, default='123456', max_length=6)
    cnpj = models.CharField(blank=False, default='11223334444555', max_length=15)
    razao_social = models.CharField(blank=True, default='sem_razao_social', max_length=100)
    nome_fantasia = models.CharField(blank=True, default='sem_nome_fantasia', max_length=100)
    modalidade = models.CharField(blank=True, default='modalidae', max_length=100)
    logradouro = models.CharField(blank=True, default='logradouro', max_length=100)
    numero = models.CharField(blank=True, default='numero', max_length=100)
    complemento = models.CharField(blank=True, default='complemento', max_length=100)
    bairro = models.CharField(blank=True, default='bairro', max_length=100)
    cidade = models.CharField(blank=True, default='cidade', max_length=100)
    uf = models.CharField(blank=True, default='uf', max_length=100)
    cep = models.CharField(blank=True, default='cep', max_length=100)
    ddd = models.CharField(blank=True, default='ddd', max_length=100)
    telefone = models.CharField(blank=True, default='telefone', max_length=100)
    fax = models.CharField(blank=True, default='fax', max_length=100)
    endereco_eletronico = models.CharField(blank=True, default='endereco_eletronico', max_length=100)
    representante = models.CharField(blank=False, default='representante', max_length=100)
    cargo_representante = models.CharField(blank=False, default='cargo_representante', max_length=100)
    data_registro_ans = models.DateField(default="1/1/2001", blank=False)

    def serialize(self):
        return {
            'id':                       f"{self.id}",
            'registro_ans':             f"{self.registro_ans}",
            'cnpj':                     f"{self.cnpj}",
            'razao_social':             f"{self.razao_social}",
            'nome_fantasia':            f"{self.nome_fantasia}",
            'modalidade':               f"{self.modalidade}",
            'logradouro':               f"{self.logradouro}",
            'numero':                   f"{self.numero}",
            'complemento':              f"{self.complemento}",
            'bairro':                   f"{self.bairro}",
            'cidade':                   f"{self.cidade}",
            'uf':                       f"{self.uf}",
            'cep':                      f"{self.cep}",
            'ddd':                      f"{self.ddd}",
            'telefone':                 f"{self.telefone}",
            'fax':                      f"{self.fax}",
            'endereco_eletronico':      f"{self.endereco_eletronico}",
            'representante':            f"{self.representante}",
            'cargo_representante':      f"{self.cargo_representante}",
            'data_registro_ans':        f"{self.data_registro_ans}",
        }


class CSVFiles(models.Model):
    csv_file = models.FileField(upload_to='csv_files')


all_models = [
    RegistroEmpresa,
    CSVFiles
]