# Importation de modules.
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages

from compte.tests import administrateur
from .models import Bureau
from .forms import BureauForm

# Création de pages webs.

def bureauPage(request): # Page du bureau.
    bureau = Bureau.objects.all()
    return render(request, 'bureau/bureau.html', {'bureau':bureau, 'title':'Page bureau'})

@user_passes_test(administrateur, login_url='connecte')
def bureau_listePage(request): # Page pour administrer les membres du bureau.  
    bureau = Bureau.objects.all()
    return render(request, 'bureau/bureau_liste.html', {'bureau':bureau, 'title':'Liste bureau'})

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
    return render(request, 'bureau/bureau_ajouter.html', {'form':form,'title':'Ajouter membre bureau'})

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
    return render(request, 'bureau/bureau_editer.html', {'form':form, 'bureau':bureau,'title':'Editer membre bureau'})