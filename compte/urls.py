# Importation de modules.
from django.urls import path
from django.contrib.auth import views

from .views import activationPage, aidePage, ajouterPage, editerPage, inscriptionPage, liste_membrePage, monprofilPage, profilePage, reunion_ajouterPage, reunion_editerPage, reunionPage, suprimerPage # Importation de vues de pages.

urlpatterns = [
    path('inscription/', inscriptionPage, name='inscrire'),
    path('connexion/', views.LoginView.as_view(template_name='compte/connexion.html', redirect_authenticated_user=False), name='connecte'),
    path('connexion/', views.LogoutView.as_view(), name='deconnecte'),
    path('activation/<uidb64>/<token>/', activationPage, name='active'),
    path('liste membres/', liste_membrePage, name='admin'), # Lien de la page d'administration'.
    path('ajouter/', ajouterPage, name='ajoute'),
    path('editer/<int:pk>/', editerPage, name='edite'),
    path('suprimer/', suprimerPage, name='suprime'),
    path('profile/', profilePage, name='profile'), # Lien de la page de profile.
    path('mon profil/', monprofilPage, name='monprofil'), # Lien de la page de mon profil.
    path('aide/', aidePage, name='aide'), # Lien de la page d'aide.
    path('reunion/', reunionPage, name='reunion'), # Lien de la page d'appel de présence.
    path('reunion ajouter/', reunion_ajouterPage, name='reunion_ajoute'), # Lien de la page d'appel de présence.
    path('reunion editer/<int:pk>/', reunion_editerPage, name='reunion_edite'), # Lien de la page d'appel de présence.
]