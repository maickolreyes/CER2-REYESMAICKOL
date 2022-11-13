from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Residencias(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "Residencia " + self.nombre

class Correspondencia(models.Model):
    tipo = models.CharField(max_length=30)

    class Estados(models.TextChoices):
        RECIBIDO = "Recibida", _('Recibido')
        ENTREGADO = "Entregada", _('Entregado')
    
    estado = models.CharField(max_length=9, choices=Estados.choices, default=Estados.RECIBIDO)
    residencia = models.ForeignKey(Residencias, on_delete=models.CASCADE)
    conserje = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name':"Conserjes"}, default=1)

    def __str__(self) -> str:
        return "Tipo Correspondencia: " + str(self.tipo) + "Estado: " + str(self.estado) + "\t" + str(self.residencia) + "Conserje Asignado: " + str(self.conserje.get_full_name())
