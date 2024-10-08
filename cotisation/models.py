# Importation de modules.
from django.utils import timezone
from django.db import models

# Création de models.

# Réunion.
class Reunion(models.Model): 
    membre = models.ForeignKey("compte.Membre", on_delete=models.CASCADE)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    presence = models.BooleanField(default=False)
    retard = models.BooleanField(default=False)
    permission = models.BooleanField(default=False)
    absence = models.BooleanField(default=False)

# Adhésion.
class MonAdhesion(models.Model): 
    membre = models.OneToOneField("compte.Membre", on_delete=models.CASCADE)
    montant = models.IntegerField(default=15000)
    reunion = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    lieu = models.CharField(max_length=50, default='Rond point Kpogli')
    paye = models.BooleanField(default=False)

# Mensuel.
class Mensuel(models.Model): 
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50, default='Rond point Kpogli')
    paye = models.BooleanField(default=False)

def __str__(self):
    return f"Mensuel de {self.membre.last_name} {self.membre.first_name}"

# Naissance.
class NouveauNe(models.Model):
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    enfant = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)

# Réjouissance.
class Rejouissance(models.Model): 
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50)
    paye = models.BooleanField(default=False)

# Don.
class Don(models.Model): 
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    objet = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)

# Décès.
class Deces(models.Model): 
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    deces = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)   

# Entrées.
class Entree(models.Model):
    libelle = models.CharField(max_length=50)
    montant = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)

# Dépenses.
class Depense(models.Model):
    libelle = models.CharField(max_length=50)
    montant = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)