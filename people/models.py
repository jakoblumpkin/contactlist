from django.db import models

# Create your models here.


class contactPerson(models.Model):
    name=models.CharField(max_length=100, null=False)
    relationship=models.CharField(max_length=100, null=True)
    number=models.CharField(max_length=13, null=True)
    notes=models.CharField(max_length=250, null=True)