# Importation de modules.
from django.urls import path

from .views import bureau_ajouterPage, bureau_editerPage, bureau_listePage, bureauPage, election_ajouterPage, election_editerPage, electionPage, ensemble_ajouterPage, ensemble_editerPage

# Création de liens de pages.
urlpatterns = [
    path('', bureauPage, name='bureau'), # Lien de la page du bureau.
    path('liste', bureau_listePage, name='bureau_liste'), # Lien vers la liste des membres du bureau.
    path('ajouter', bureau_ajouterPage, name='bureau_ajoute'), # Lien vers la page pour ajouter um membre du bureau.
    path('editer/<int:pk>/', bureau_editerPage, name='bureau_edite'), # Lien vers la page pour modifier um membre du bureau.
    path('photo ensemble/ajouter', ensemble_ajouterPage, name='ensemble_ajoute'), # Lien vers la page pour ajouter ume photo d'ensemble du bureau.
    path('photo ensemble/<int:pk>/éditer', ensemble_editerPage, name='ensemble_edite'), # Lien vers la page pour modifier ume photo d'ensemble du bureau.
    path('election', electionPage, name='election'), # Lien vers les résultats des élections.
    path('election ajouter', election_ajouterPage, name='election_ajoute'), # Lien vers la page pour ajouter les résultats des élections.
    path('election editer/<int:pk>/', election_editerPage, name='election_edite'), # Lien vers la page pour modifier les résultats des élections.
]