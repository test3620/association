# importation de modules.
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum

from compte.tests import administrateur
from .forms import AdhesionForm, DecesForm, DepenseForm, DonForm, EntreeForm, MensuelForm, NaissanceForm, RejouissanceForm
from .models import Deces, Depense, Don, Entree, Mensuel, MonAdhesion, NouveauNe, Rejouissance

# Création de vues de page.

# Adhésion.
@user_passes_test(administrateur, login_url='connecte')
def adhesionPage(request): # Page d'adhésion.
    adhesion = MonAdhesion.objects.all() # Afficher l'adhésion de tout les membres.
    # Total d'adhésion payée et impyéé de tous les membres.
    payer_adhesion = MonAdhesion.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_adhesion = MonAdhesion.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # Convertir la valeur None à 0.
    if payer_adhesion is None:
        payer_adhesion = 0
    if impayer_adhesion is None:
        impayer_adhesion = 0
    return render(request, 'cotisation/adhesion.html', {
        'adhesion':adhesion,
        'payer_adhesion':payer_adhesion,
        'impayer_adhesion':impayer_adhesion,
        })

@user_passes_test(administrateur, login_url='connecte')
def adhesion_ajouterPage(request): # Page pour ajouter l'adhésion.
    if request.method  == 'POST':
        form = AdhesionForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Adhésion créée pour { membre }")
            return redirect('adhesion')
    else:
        form = MensuelForm()
    return render(request, 'cotisation/adhesion_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def adhesion_editerPage(request, pk): # Page de modification d'adhésion.
    adhesion = MonAdhesion.objects.get(id=pk)
    if request.method  == 'POST':
        form = AdhesionForm(request.POST, instance=adhesion)
        if form.is_valid():
            form.save()
            messages.success(request, f"Adhésion modifiée pour { adhesion.membre.last_name } { adhesion.membre.first_name }")
            return redirect('adhesion')
    else:
        form = MensuelForm(instance=adhesion)
    return render(request, 'cotisation/adhesion_editer.html', {'form':form, 'adhesion':adhesion})

# Mensuel.
@user_passes_test(administrateur, login_url='connecte')
def mensuelPage(request): # Page du mensuel.
    mensuel = Mensuel.objects.all()
    # Total des mensuels payée et impyéé de tous les membres.
    payer_mensuel = Mensuel.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_mensuel = Mensuel.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # Convertir la valeur None à 0.
    if payer_mensuel is None:
        payer_mensuel = 0
    if impayer_mensuel is None:
        impayer_mensuel = 0
    return render(request, 'cotisation/mensuel.html', {
        'mensuel':mensuel, 
        'payer_mensuel':payer_mensuel, 
        'impayer_mensuel':impayer_mensuel
        })

@user_passes_test(administrateur, login_url='connecte')
def mensuel_ajouterPage(request): # Page pour ajouter le mensuel.
    if request.method  == 'POST':
        form = MensuelForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Mensuel créé pour { membre }")
            return redirect('mensuel')
    else:
        form = MensuelForm()
    return render(request, 'cotisation/mensuel_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def mensuel_editerPage(request, pk): # Page de modification mensuel.
    mensuel = Mensuel.objects.get(id=pk)
    if request.method  == 'POST':
        form = MensuelForm(request.POST, instance=mensuel)
        if form.is_valid():
            form.save()
            messages.success(request, f"Mensuel modifiée pour  { mensuel.membre.last_name } { mensuel.membre.first_name }")
            return redirect('mensuel')
    else:
        form = MensuelForm(instance=mensuel)
    return render(request, 'cotisation/mensuel_editer.html', {'form':form, 'mensuel':mensuel})

# Naissance.
@user_passes_test(administrateur, login_url='connecte')
def naissancePage(request): # Page de naissance.
    naissance = NouveauNe.objects.all()
    # Total de naissnece payée et impayée de tous les membres.
    payer_naissance = NouveauNe.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_naissance = NouveauNe.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # Convertir la valeur None à 0.
    if payer_naissance is None:
        payer_naissance = 0
    if impayer_naissance is None:
        impayer_naissance = 0
    return render(request, 'cotisation/naissance.html', {
        'naissance':naissance,
        'payer_naissance':payer_naissance,
        'impayer_naissance':impayer_naissance
        })

@user_passes_test(administrateur, login_url='connecte')
def naissance_ajouterPage(request): # Page pour ajouter la naissance.
    if request.method  == 'POST':
        form = NaissanceForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Naissance créée pour { membre }")
            return redirect('naissance')
    else:
        form = NaissanceForm()
    return render(request, 'cotisation/naissance_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def naissance_editerPage(request, pk): # Page de modification de naissance.
    naissance = NouveauNe.objects.get(id=pk)
    if request.method  == 'POST':
        form = NaissanceForm(request.POST, instance=naissance)
        if form.is_valid():
            form.save()
            messages.success(request, f"Naissance modifiée pour { naissance.membre.last_name } { naissance.membre.first_name }")
            return redirect('naissance')
    else:
        form = NaissanceForm(instance=naissance)
    return render(request, 'cotisation/naissance_editer.html', {'form':form, 'naissance':naissance})

# Réjouissance.
@user_passes_test(administrateur, login_url='connecte')
def rejouissancePage(request): # Page de Réjoussance.
    rejouissance = Rejouissance.objects.all()
    # Total de réjouissance payée et impayée de tous les membres.
    payer_rejouissance = Rejouissance.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_rejouissance = Rejouissance.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # Convertir la valeur None à 0.
    if payer_rejouissance is None:
        payer_rejouissance = 0
    if impayer_rejouissance is None:
        impayer_rejouissance = 0
    return render(request, 'cotisation/rejouissance.html', {
        'rejouissance':rejouissance,
        'payer_rejouissance': payer_rejouissance,
        'impayer_rejouissance': impayer_rejouissance
        })

@user_passes_test(administrateur, login_url='connecte')
def rejouissance_ajouterPage(request): # Page pour ajouter la réjouissance.
    if request.method  == 'POST':
        form = RejouissanceForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Réjouissance créée pour { membre }")
            return redirect('rejouissance')
    else:
        form = RejouissanceForm()
    return render(request, 'cotisation/rejouissance_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def rejouissance_editerPage(request, pk): # Page de modification de réjouissance.
    rejouissance = Rejouissance.objects.get(id=pk)
    if request.method  == 'POST':
        form = RejouissanceForm(request.POST, instance=rejouissance)
        if form.is_valid():
            form.save()
            messages.success(request, f"Réjouissance modifiée pour { rejouissance.membre.last_name } { rejouissance.membre.first_name }")
            return redirect('rejouissance')
    else:
        form = RejouissanceForm(instance=rejouissance)
    return render(request, 'cotisation/rejouissance_editer.html', {'form':form, 'rejouissance':rejouissance})

# Don.
@user_passes_test(administrateur, login_url='connecte')
def donPage(request): # Page de Don.
    don = Don.objects.all()
    # Total de don payé et impayé de tous les membres.
    payer_don = Don.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_don = Don.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # Convertir la valeur None à 0.
    if payer_don is None:
        payer_don = 0
    if impayer_don is None:
        impayer_don = 0
    return render(request, 'cotisation/don.html', {'don':don, 'payer_don':payer_don, 'impayer_don':impayer_don})

@user_passes_test(administrateur, login_url='connecte')
def don_ajouterPage(request): # Page pour ajouter le don.
    if request.method  == 'POST':
        form = DonForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Don créée pour { membre }")
            return redirect('don')
    else:
        form = DonForm()
    return render(request, 'cotisation/don_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def don_editerPage(request, pk): # Page de modification de don.
    don = Don.objects.get(id=pk)
    if request.method  == 'POST':
        form = DonForm(request.POST, instance=don)
        if form.is_valid():
            form.save()
            messages.success(request, f"Don modifiée pour { don.membre.last_name } { don.membre.first_name }")
            return redirect('don')
    else:
        form = DonForm(instance=don)
    return render(request, 'cotisation/don_editer.html', {'form':form, 'don':don})


# Décès.
@user_passes_test(administrateur, login_url='connecte')
def decesPage(request): # Page de Décès.
    deces = Deces.objects.all()
    # Total de décès payé et impayé de tous les membres.
    payer_deces = Deces.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_deces = Deces.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # Convertir la valeur None à 0.
    if payer_deces is None:
        payer_deces = 0
    if impayer_deces is None:
        impayer_deces = 0
    return render(request, 'cotisation/deces.html', {
        'deces':deces, 
        'payer_deces':payer_deces, 
        'impayer_deces':impayer_deces
        })

@user_passes_test(administrateur, login_url='connecte')
def deces_ajouterPage(request): # Page pour ajouter un décès.
    if request.method  == 'POST':
        form = DecesForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Décès créée pour { membre }")
            return redirect('deces')
    else:
        form = DecesForm()
    return render(request, 'cotisation/deces_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def deces_editerPage(request, pk): # Page de modification de décès.
    deces = Deces.objects.get(id=pk)
    if request.method  == 'POST':
        form = DecesForm(request.POST, instance=deces)
        if form.is_valid():
            form.save()
            messages.success(request, f"Décès modifiée pour { deces.membre.last_name } { deces.membre.first_name }")
            return redirect('deces')
    else:
        form = DecesForm(instance=deces)
    return render(request, 'cotisation/deces_editer.html', {'form':form, 'deces':deces})


# Comptabilité.
@user_passes_test(administrateur, login_url='connecte')
def comptabilitePage(request): # Page de Comptabilité.
    entree = Entree.objects.all() 
    depense = Depense.objects.all()    
    # Total des entrées et dépenses de l'AJRDL.
    total_entree = Entree.objects.aggregate(total=Sum('montant'))['total']
    total_depense = Depense.objects.aggregate(total=Sum('montant'))['total']
    # La conversion de la valeur None à 0 (chifre zéro).
    if total_entree is None:
        total_entree = 0
    if total_depense is None:
        total_depense = 0
    # Total payée et impayée de chaque cotisation des membres.
    payer_adhesion = MonAdhesion.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_adhesion = MonAdhesion.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_mensuel = Mensuel.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_mensuel = Mensuel.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_naissance = NouveauNe.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_naissance = NouveauNe.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_rejouissance = Rejouissance.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_rejouissance = Rejouissance.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_don = Don.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_don = Don.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_deces = Deces.objects.filter(paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_deces = Deces.objects.filter(paye=False).aggregate(Sum('montant'))['montant__sum']
    # La conversion de la valeur None à 0 (chifre zéro).
    if payer_adhesion is None:
        payer_adhesion = 0
    if impayer_adhesion is None:
        impayer_adhesion = 0
    if payer_mensuel is None:
        payer_mensuel = 0
    if impayer_mensuel is None:
        impayer_mensuel = 0
    if payer_naissance is None:
        payer_naissance = 0
    if impayer_naissance is None:
        impayer_naissance = 0
    if payer_rejouissance is None:
        payer_rejouissance = 0
    if impayer_rejouissance is None:
        impayer_rejouissance = 0
    if payer_don is None:
        payer_don = 0
    if impayer_don is None:
        impayer_don = 0
    if payer_deces is None:
        payer_deces = 0
    if impayer_deces is None:
        impayer_deces = 0
    # Total payé et impayé de tous les membres.
    total_paye = payer_adhesion + payer_mensuel + payer_naissance + payer_rejouissance + payer_don + payer_deces
    total_impaye = impayer_adhesion + impayer_mensuel + impayer_naissance + impayer_rejouissance + impayer_don + impayer_deces
    solde = (total_paye + total_entree) - total_depense
    return render(request, 'cotisation/comptabilite.html', {
        'depense': depense, 
        'entree': entree,
        'total_entree': total_entree,
        'total_depense': total_depense,
        'total_paye': total_paye,
        'total_impaye': total_impaye,
        'solde': solde
        })


# Entrées.
@user_passes_test(administrateur, login_url='connecte')
def entree_ajouterPage(request): # Page pour ajouter une entrée .
    if request.method  == 'POST':
        form = EntreeForm(request.POST)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            form.save()
            messages.success(request, f"Versement effectué pour { libelle }")
            return redirect('comptable')
    else:
        form = EntreeForm()
    return render(request, 'cotisation/entree_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def entree_editerPage(request, pk): # Page de modification d'une entrée.
    entree = Entree.objects.get(id=pk)
    if request.method  == 'POST':
        form = EntreeForm(request.POST, instance=entree)
        if form.is_valid():
            form.save()
            messages.success(request, f"Versement de { entree.libelle } modifiée !")
            return redirect('comptable')
    else:
        form = EntreeForm(instance=entree)
    return render(request, 'cotisation/entree_editer.html', {'form':form, 'entree':entree})


# Dépenses.
@user_passes_test(administrateur, login_url='connecte')
def depense_ajouterPage(request): # Page pour ajouter une dépense effectuée.
    if request.method  == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            form.save()
            messages.success(request, f"Dépense effectuée pour { libelle }")
            return redirect('comptable')
    else:
        form = DepenseForm()
    return render(request, 'cotisation/depense_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def depense_editerPage(request, pk): # Page de modification de dépense.
    depense = Depense.objects.get(id=pk)
    if request.method  == 'POST':
        form = DepenseForm(request.POST, instance=depense)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dépense de { depense.libelle } modifiée !")
            return redirect('comptable')
    else:
        form = DepenseForm(instance=depense)
    return render(request, 'cotisation/depense_editer.html', {'form':form, 'depense':depense})