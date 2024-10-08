# Importation de modules.
from django.contrib import admin

from bureau.models import Bureau, Contact, Diaporama, Election, Ensemble, Galerie

# Enrégistrement de models.

admin.site.register(Bureau) # Models du Bureau.
admin.site.register(Election) # Models des Élections du Bureau.
admin.site.register(Galerie) # Models Galerie.
admin.site.register(Diaporama) # Models Diaporama.
admin.site.register(Contact) # Models Contact.
admin.site.register(Ensemble) # Models Ensemble.
