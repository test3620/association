from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
#from django.db.models import Sum

from compte.tests import administrateur
from cotisation.forms import ReunionForm
from cotisation.models import Reunion 
from compte.models import Membre # Importation du model membre.

# CREATION DE PAGES (VUES)

def accueilPage(request): # Page d'accueil.
    return render(request, 'index.html', {'title':'Accueil'})

def contactPage(request): # Page de contact de l'AJRDL.
    return render(request, 'contact.html', {'title':'Contact'})

def membrePage(request): # Page de membres.
    membre = Membre.objects.all() # Récupérqtion de tous les membre.
    return render(request, 'membre.html', {'membre':membre, 'title':'Espace membre'})

def reglementPage(request): # Page de règlements intérieurs.
    return render(request, 'reglement.html', {'title':'Règlement'})

def statutPage(request): # Page de statut.
    return render(request, 'statut.html', {'title':'Statut'})

def projetPage(request): # Page de projets.
    return render(request, 'projet.html', {'title':'Projets'})

def visionPage(request): # Page de visions.
    return render(request, 'vision.html', {'title':'Vision'})

def informationPage(request): # Page d'information.
    return render(request, 'information.html', {'title':'Information'})

def realisationPage(request): # Page de réalisation.
    return render(request, 'realisation.html', {'title':'Réalisation'})


