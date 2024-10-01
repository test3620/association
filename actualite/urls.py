# Importation de modules.
from django.urls import path

from .views import actualite_ajouterPage, actualite_editerPage, actualite_listePage, actualitePage, commentaire_ajouterPage, commentaire_editerPage, commentaire_listePage, detailPage

# Création de liens de pages.
urlpatterns = [
    path('', actualitePage, name='actualite'), # Lien de la page d'actualité.
    path('detail/<str:pk>/', detailPage, name='detail'), # Lien de la page de detail des actualités.
    path('liste/', actualite_listePage, name='actualite_liste'), # Lien vers une page d'administration.
    path('ajouter/', actualite_ajouterPage, name='actualite_ajoute'), # Lien vers une page pour ajouter d'actualités.
    path('editer/<int:pk>/', actualite_editerPage, name='actualite_edite'), # Lien vers une page pour éditer l'actualité.
    path('Commentaire/', commentaire_listePage, name='commentaire_liste'), # Lien vers une page pour administrer un commentaire.
    path('commentaire ajouter/', commentaire_ajouterPage, name='commentaire_ajoute'), # Lien vers une page pour ajouter de commentaires.
    path('commentairer activer/<int:pk>/', commentaire_editerPage, name='commentaire_edite'), # Lien vers une page pour activer le commentaire.
]