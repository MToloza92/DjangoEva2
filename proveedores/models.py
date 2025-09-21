from django.db import models

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.razon_social
