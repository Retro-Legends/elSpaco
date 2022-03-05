from django.db import models
from django.forms import CharField, DateTimeField
import uuid


class Cladire(models.Model):
    codCladire = models.AutoField(primary_key=True)
    denCladire = models.CharField(max_length=30)
    adresaCladire = models.CharField(max_length=200)
    nrEtaje = models.IntegerField()
    # nrBirouri = models.IntegerField()

    def __str__(self) -> str:
        return self.denCladire
