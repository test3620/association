from django.contrib import admin

from .models import Deces, Depense, Don, Entree, Mensuel, MonAdhesion, NouveauNe, Rejouissance, Reunion

# Enrégistrement de models.

admin.site.register(Reunion)
admin.site.register(MonAdhesion)
admin.site.register(Mensuel)
admin.site.register(NouveauNe)
admin.site.register(Rejouissance)
admin.site.register(Don)
admin.site.register(Deces)
admin.site.register(Depense)
admin.site.register(Entree)