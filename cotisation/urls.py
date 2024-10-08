# Importation de modules.
from django.urls import path

from .views import adhesion_ajouterPage, adhesion_editerPage, adhesionPage, comptabilitePage, deces_ajouterPage, deces_editerPage, decesPage, depense_ajouterPage, depense_editerPage, don_ajouterPage, don_editerPage, donPage, entree_ajouterPage, entree_editerPage, mensuel_ajouterPage, mensuel_editerPage, mensuelPage, naissance_ajouterPage, naissance_editerPage, naissancePage, rejouissance_ajouterPage, rejouissance_editerPage, rejouissancePage # Importation de vues de pages.

urlpatterns = [
    path('mensuel/', mensuelPage, name='mensuel'),
    path('mensuel ajoute/', mensuel_ajouterPage, name='mensuel_ajoute'),    
    path('mensuel edite/<int:pk>/', mensuel_editerPage, name='mensuel_edite'),    
    path('adhesion/', adhesionPage, name='adhesion'),
    path('adhesion ajoutee/', adhesion_ajouterPage, name='adhesion_ajoute'),    
    path('adhesion editee/<int:pk>/', adhesion_editerPage, name='adhesion_edite'),   
    path('naissance/', naissancePage, name='naissance'),
    path('naissance ajoutee/', naissance_ajouterPage, name='naissance_ajoute'),    
    path('naissance editee/<int:pk>/', naissance_editerPage, name='naissance_edite'),  
    path('rejouissance/', rejouissancePage, name='rejouissance'),
    path('rejouissance ajoutee/', rejouissance_ajouterPage, name='rejouissance_ajoute'),    
    path('rejouissance editee/<int:pk>/', rejouissance_editerPage, name='rejouissance_edite'),  
    path('don/', donPage, name='don'),
    path('don ajoutee/', don_ajouterPage, name='don_ajoute'),    
    path('don editee/<int:pk>/', don_editerPage, name='don_edite'),  
    path('deces/', decesPage, name='deces'),
    path('deces ajoutee/', deces_ajouterPage, name='deces_ajoute'),    
    path('deces editee/<int:pk>/', deces_editerPage, name='deces_edite'),  
    path('', comptabilitePage, name='comptable'),
    path('entree ajoutee/', entree_ajouterPage, name='entree_ajoute'),    
    path('entree editee/<int:pk>/', entree_editerPage, name='entree_edite'),  
    path('depense ajoutee/', depense_ajouterPage, name='depense_ajoute'),    
    path('depense editee/<int:pk>/', depense_editerPage, name='depense_edite'),  
]