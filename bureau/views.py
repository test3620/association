# Importation de modules.
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages

from compte.tests import administrateur
from .models import Bureau, Election, Ensemble
from .forms import BureauForm, ElectionForm, EnsembleForm

# Création de pages webs.

# Bureau.
def bureauPage(request): # Page du bureau.
    bureau = Bureau.objects.all()
    election = Election.objects.all()
    ensemble = Ensemble.objects.all()
    return render(request, 'bureau/bureau.html', {
        'bureau':bureau, 
        'ensemble':ensemble, 
        'election':election, 
        'title':'Page bureau'
        })

@user_passes_test(administrateur, login_url='connecte')
def bureau_listePage(request): # Page pour administrer les membres du bureau.  
    bureau = Bureau.objects.all()
    ensemble = Ensemble.objects.all()
    return render(request, 'bureau/bureau_liste.html', {
        'bureau':bureau, 
        'ensemble':ensemble, 
        'title':'Liste bureau'
        })

@user_passes_test(administrateur, login_url='connecte')
def bureau_ajouterPage(request): # Page pour ajouter un membre du bureau.
    if request.method == "POST":
        form = BureauForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            messages.success(request, f"Un nouveau membre du bureau { nom } { prenom } a été ajouté avec succès.")
            form.save()
            return redirect('bureau_liste')
    else:
        form = BureauForm()
    return render(request, 'bureau/bureau_ajouter.html', {
        'form':form, 
        'title':'Ajouter membre bureau'
        })

@user_passes_test(administrateur, login_url='connecte')
def bureau_editerPage(request, pk): # Page pour éditer un membre du bureau.
    bureau = Bureau.objects.get(id=pk)
    if request.method == "POST":
        form = BureauForm(request.POST, request.FILES, instance=bureau)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            messages.success(request, f"Modification réusie avec succès au membre du bureau { nom } { prenom }.")
            form.save()
            return redirect('bureau_liste')
    else:
        form = BureauForm(instance=bureau)
    return render(request, 'bureau/bureau_editer.html', {
        'form':form, 
        'bureau':bureau, 
        'title':'Editer membre bureau'
        })


# Photo d'ensemble du bureau.
@user_passes_test(administrateur, login_url='connecte')
def ensemble_ajouterPage(request): # Page pour ajouter un d'ensemble du bureau.
    if request.method == "POST":
        form = EnsembleForm(request.POST, request.FILES)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            messages.success(request, f"Photo d'ensemble du bureau { titre } ajoutée.")
            form.save()
            return redirect('bureau_liste')
    else:
        form = EnsembleForm()
    return render(request, 'bureau/ensemble_ajouter.html', {
        'form':form, 
        'title':'Ajouter photo ensemble'
        })

@user_passes_test(administrateur, login_url='connecte')
def ensemble_editerPage(request, pk): # Page pour éditer une photo d'ensemble du bureau.
    ensemble = Ensemble.objects.get(id=pk)
    if request.method == "POST":
        form = EnsembleForm(request.POST, request.FILES, instance=ensemble)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            messages.success(request, f"Photo d'ensemble du bureau { titre } modifiée.")
            form.save()
            return redirect('bureau_liste')
    else:
        form = EnsembleForm(instance=ensemble)
    return render(request, 'bureau/ensemble_editer.html', {
        'form':form, 
        'ensemble':ensemble, 
        'title':'Photo ensemble éditée'
        })


# Elections.
@user_passes_test(administrateur, login_url='connecte')
def electionPage(request): # Page pour administrer les élections du bureau.  
    election = Election.objects.all()
    return render(request, 'bureau/election.html', {
        'election':election, 
        'title':'Résultats électoraux'
        })

@user_passes_test(administrateur, login_url='connecte')
def election_ajouterPage(request): # Page pour ajouter les résultat des élection du bureau.
    if request.method == "POST":
        form = ElectionForm(request.POST)
        if form.is_valid():          
            messages.success(request, f"Résultats des élections du bureau ajoutés avec succès.")
            form.save()
            return redirect('election')
    else:
        form = ElectionForm()
    return render(request, 'bureau/election_ajouter.html', {
        'form':form, 
        'title':'Ajouter résultats'
        })

@user_passes_test(administrateur, login_url='connecte')
def election_editerPage(request, pk): # Page pour éditer les résultats des élections du bureau.
    election = Election.objects.get(id=pk)
    if request.method == "POST":
        form = ElectionForm(request.POST, instance=election)
        if form.is_valid():
            messages.success(request, f"Modification faites sur les résultats des élections du bureau.")
            form.save()
            return redirect('election')
    else:
        form = ElectionForm(instance=election)
    return render(request, 'bureau/election_editer.html', {
        'form':form, 
        'election':election, 
        'title':'Editer membre bureau'
        })