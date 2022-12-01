from django.db import models

# Create your models here.
class Pet(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    raca = models.CharField(max_length=20, null=True, blank=True)
    SEXO_CHOICES = (
        ('M', 'Macho'),
        ('F', 'Fêmea'),
        ('Escolha uma opção', 'Escolha uma opção'),
    )
    TIPO_CHOICES = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Outro', 'Outro'),
        ('Escolha uma opção', 'Escolha uma opção'),
    )
    PORTE_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )
    PELO_CHOICES = (
        ('C', 'Curto'),
        ('L', 'Longo'),
        ('S P', 'Sem Pelo'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False, default='Escolha uma opção')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, blank=False, null=False, default='Escolha uma opção')
    porte = models.CharField(max_length=10, choices=PORTE_CHOICES, blank=False, null=False, default='Escolha uma opção')
    pelo = models.CharField(max_length=10, choices=PELO_CHOICES, blank=False, null=False, default='Escolha uma opção')
    descrição = models.TextField()

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=32)
    telefone = models.IntegerField(max_length=20)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

class Ong(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=32)
    telefone = models.IntegerField(max_length=20)
    cnpj = models.IntegerField(max_length=14)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.IntegerField(max_length=8)
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.rua

class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
