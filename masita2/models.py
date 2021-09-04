from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Register(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
