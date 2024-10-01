# Importation de modules.
from django.db import models
from django.utils import timezone

# Céation de model.

class Actualite(models.Model): # Model d'actualité.
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualite/', height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey("compte.Membre", on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
    

class Commentaire(models.Model): # Model du commentaire d'actualité.
    actualite = models.ForeignKey('Actualite', on_delete=models.CASCADE, related_name='comments')
    nom = models.CharField(max_length=80)
    contenu = models.CharField(max_length=50000)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    photo = models.ImageField(default="default.jpg", upload_to="membre/identite/", height_field=None, width_field=None, max_length=None)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'Commentaire {self.contenu} de {self.nom}'