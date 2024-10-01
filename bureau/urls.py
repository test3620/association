# Importation de modules.
from django.urls import path

from .views import bureau_ajouterPage, bureau_editerPage, bureau_listePage, bureauPage

# Création de liens de pages.
urlpatterns = [
    path('', bureauPage, name='bureau'), # Lien de la page du bureau.
    path('liste', bureau_listePage, name='bureau_liste'), # Lien vers la liste des membres du bureau.
    path('ajouter', bureau_ajouterPage, name='bureau_ajoute'), # Lien vers la page pour ajouter um membre du bureau.
    path('editer/<int:pk>/', bureau_editerPage, name='bureau_edite'), # Lien vers la page pour modifier um membre du bureau.
]