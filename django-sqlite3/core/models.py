from django.db import models

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantidade em Estoque')


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)