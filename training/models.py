from django.db import models
from multiselectfield import MultiSelectField


              

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)


class Module(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

class Session(models.Model):
    modules = tuple(Module.objects.all().values_list('nom', 'nom'))

    nom = models.CharField(max_length=200)
    start_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    module_ids = MultiSelectField(choices=modules, max_length=254)


class Inscription(models.Model):
    etudiant_id = models.ForeignKey(Etudiant, null=True, on_delete=models.SET_NULL)
    session_id = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    montant = models.FloatField()

