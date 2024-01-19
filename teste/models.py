from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)

    def __str__(self):
        return self.modelo
    
