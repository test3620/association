from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import accueilPage, contactPage, informationPage, membrePage, projetPage, realisationPage, reglementPage, statutPage, visionPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilPage, name='accueil'), # Lien de la page d'accueil.
    path('actualite/', include('actualite.urls')), # Lien de la page d'actualité.
    path('bureau/', include('bureau.urls')), # Lien de la page du bureau.
    path('compte/', include('compte.urls')), # Lien de la page d'utilisateur.
    path('cotisation/', include('cotisation.urls')), # Lien de la page de cotisations.
    path('contact/', contactPage, name='contact'), # Lien de la page de contact.
    path('membre/', membrePage, name='membre'), # Lien de la page de membre.
    path('reglement/', reglementPage, name='reglement'), # Lien de la page de règlement.
    path('statut/', statutPage, name='statut'), # Lien de la page de statut.
    path('projet/', projetPage, name='projet'), # Lien de la page de projets.
    path('vision/', visionPage, name='vision'), # Lien de la page de visions.
    path('information/', informationPage, name='information'), # Lien de la page d'information.
    path('realisation/', realisationPage, name='realisation'), # Lien de la page de réalisation.
    path('summernote/', include('django_summernote.urls')), # Lien de la page d'utilisateur.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)