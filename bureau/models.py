from django.db import models

# Céation de model.

class Bureau(models.Model): # Model du bureau.
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='bureau', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Bureau'
        verbose_name_plural = 'Bureau'

    def __str__(self):
        return f"{self.nom} {self.prenom}"   