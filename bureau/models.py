from django.db import models
#from django.utils import timezone

# Céation de model.

# Model du bureau.
class Bureau(models.Model): 
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='bureau', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f"{self.nom} {self.prenom}"   
    
# Model de photo d'ensemble.
class Ensemble(models.Model):    
    titre = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='bureau/ensemble', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f"Titre de photo d'ensemble est: {self.titre}"   
    
# Modèle des élections.
class Election(models.Model):
    president = models.IntegerField()
    secretaire = models.IntegerField()
    secretaire_adjoint = models.IntegerField()
    tresorier = models.IntegerField()
    tresorier_adjoint = models.IntegerField()
    conseiller_1 = models.IntegerField()
    conseiller_2 = models.IntegerField()

# Modèle de galerie.
class Galerie(models.Model):
    REUNION = "Réunion"
    FETE = "Fête"
    DECES = "Décès"
    TITRE = {
        REUNION : "Réunion",
        FETE : "Fête",
        DECES : "Décès"
    }

    titre = models.CharField(max_length=50, choices=TITRE, default=REUNION,)
    intitule = models.CharField(max_length=50)
    image = models.ImageField(upload_to='galerie/', height_field=None, width_field=None, max_length=None)
    date = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.titre} {self.intitule}'
    

# Modèle de diaporama.
class Diaporama(models.Model):
    REUNION = "Réunion"
    FETE = "Fête"
    DECES = "Décès"
    TITRE = {
        REUNION : "Réunion",
        FETE : "Fête",
        DECES : "Décès"
    }

    titre = models.CharField(max_length=50, choices=TITRE, default=REUNION,)
    intitule = models.CharField(max_length=50)
    image = models.ImageField(upload_to='diaporama/', height_field=None, width_field=None, max_length=None)
    date = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.titre} {self.intitule}'
    

# Modèle de contact.
class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{ self.date } { self.prenom } a envoyé { self.sujet }'