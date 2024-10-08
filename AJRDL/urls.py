# Importation de modules.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import accueilPage, contact_detailPage, contact_listePage, contact_suprimerPage, contactPage, diaporama_ajouterPage, diaporama_editerPage, diaporama_listePage, galerie_ajouterPage, galerie_editerPage, galerie_listePage, informationPage, membrePage, projetPage, realisationPage, reglementPage, statutPage, visionPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilPage, name='accueil'), # Lien de la page d'accueil.
    path('actualite/', include('actualite.urls')), # Lien de la page d'actualité.
    path('bureau/', include('bureau.urls')), # Lien de la page du bureau.
    path('compte/', include('compte.urls')), # Lien de la page d'utilisateur.
    path('comptabilite/', include('cotisation.urls')), # Lien de la page de cotisations.
    path('contact/', contactPage, name='contact'), # Lien de la page de contact.
    path('contact/liste', contact_listePage, name='contact_liste'), # Lien de liste de contact.
    path('contact/<int:pk>/détailler', contact_detailPage, name='contact_detail'), # Lien detail de contact.
    path('contact/<int:pk>/suprimer', contact_suprimerPage, name='contact_suprime'), # Lien de supression de contact.
    path('membre/', membrePage, name='membre'), # Lien de la page de membre.
    path('reglement/', reglementPage, name='reglement'), # Lien de la page de règlement.
    path('statut/', statutPage, name='statut'), # Lien de la page de statut.
    path('projet/', projetPage, name='projet'), # Lien de la page de projets.
    path('vision/', visionPage, name='vision'), # Lien de la page de visions.
    path('information/', informationPage, name='information'), # Lien de la page d'information.
    path('realisation/', realisationPage, name='realisation'), # Lien de la page de réalisation.
    path('galerie/', galerie_listePage, name='galerie'), # Lien de la page de galerie.
    path('galerie/ajouter', galerie_ajouterPage, name='galerie_ajoute'), # Lien pour ajouter de galerie.
    path('galerie/<int:pk>/editer', galerie_editerPage, name='galerie_edite'), # Lien pour éditer de galerie.
    path('diaporama/', diaporama_listePage, name='diaporama'), # Lien de la page de diaporama.
    path('diaporama/ajouter', diaporama_ajouterPage, name='diaporama_ajoute'), # Lien pour ajouter de diaporama.
    path('diaporama/<int:pk>/editer', diaporama_editerPage, name='diaporama_edite'), # Lien pour éditer de diaporama.
    path('summernote/', include('django_summernote.urls')), # Lien de la page d'utilisateur.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)