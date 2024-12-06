from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    nif = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    endereco = models.CharField(max_length=50)
    numero_de_conta = models.IntegerField()
    numero_do_contador = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    

class CarregarRecarga(models.Model):
    id_do_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    codigo_da_recarga = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo_da_recarga