# Importation de modules.
from django.utils import timezone
from django.db import models

# Création de models.

class Reunion(models.Model): # Réunion.
    membre = models.ForeignKey("compte.Membre", on_delete=models.CASCADE)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    presence = models.BooleanField(default=False)
    retard = models.BooleanField(default=False)
    permission = models.BooleanField(default=False)
    absence = models.BooleanField(default=False)


class MonAdhesion(models.Model): # Adhésion.
    membre = models.OneToOneField("compte.Membre", on_delete=models.CASCADE)
    montant = models.IntegerField(default=15000)
    reunion = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    lieu = models.CharField(max_length=50, default='Rond point Kpogli')
    paye = models.BooleanField(default=False)


class Mensuel(models.Model): # Mensuel.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50, default='Rond point Kpogli')
    paye = models.BooleanField(default=False)

def __str__(self):
    return f"Mensuel de {self.membre.last_name} {self.membre.first_name}"


class NouveauNe(models.Model): # Naissance.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    enfant = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)


class Rejouissance(models.Model): # Réjouissance.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50)
    paye = models.BooleanField(default=False)


class Don(models.Model): # Don.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    objet = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)


class Deces(models.Model): # Décès:
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    deces = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)   