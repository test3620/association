# Importation de modules django.
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.db.models import Sum

from cotisation.forms import ReunionForm
from cotisation.models import Deces, Don, Mensuel, MonAdhesion, NouveauNe, Rejouissance, Reunion
from .tests import administrateur
from .models import Membre
from .forms import EditerForm, MembreForm, MotDePasseChangerForm # Importation du formulaire d'inscription.

# Création de vues de pages.

# Page d'inscription.
def inscriptionPage(request): 
    if request.method == 'POST':
        form = MembreForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Désactiver le compte jusqu'à ce que l'utilisateur clique sur le lien de confirmation.
            nom = form.cleaned_data.get('last_name')
            prenom = form.cleaned_data.get('first_name')
            messages.success(request, f"Compte créé avec succès au membre { nom } { prenom }.")
            messages.warning(request, "Veuillez l'activé dans votre mail pour se connecter !")
            user.save()

            # Message de confirmation du compte.
            current_site = get_current_site(request)
            mail_subject = 'Activation de votre compte AJRDL'
            message = render_to_string('compte/confirmation.html', {
                'nom': nom,
                'prenom': prenom,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = user.email
            send_mail(mail_subject, message, 'kpoutou700@gmail.com', [to_email])

            form = MembreForm() # Retourner le formulaire vide.
    else:
        form = MembreForm()
    return render(request, 'compte/inscription.html', {'title':'Inscription', 'form':form})

def activationPage(request, uidb64, token): # Page d'activation du compte d'un membre.
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Votre compte est activé. Connectez vous maintenant.')
        return redirect('connecte')
    else:
        messages.info(request, 'Compte déjà activé. connectez vous !')
        return redirect('connecte')   

# Page d'administration.
@user_passes_test(administrateur, login_url='connecte')
def liste_membrePage(request): 
    membres = Membre.objects.all() # Afficher tous les membres.
    effectif = Membre.objects.all().count() # Effectif des membres.
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
    return render(request, 'compte/liste_membre.html', {
        'membre':membres, 
        'effectif':effectif,
        'total_paye':total_paye,
        'total_impaye':total_impaye,
        'title':'Administration'
        })

# Page pour ajouter un membre.
@user_passes_test(administrateur, login_url='connecte')
def ajouterPage(request): 
    if request.method == 'POST':
        form = MembreForm(request.POST, request.FILES)
        if form.is_valid(): 
            nom = form.cleaned_data.get('last_name')
            prenom = form.cleaned_data.get('first_name')
            messages.success(request, f"Compte créé avec succès au membre { nom } { prenom }.")
            form.save()
            return redirect('admin') # Retourner à la page admin.
    else:
        form = MembreForm()
    return render(request, 'compte/ajouter.html', {'form':form})

# Page pour éditer/modifier un membre.
@user_passes_test(administrateur, login_url='connecte')
def editerPage(request, pk): 
    membre = Membre.objects.get(id=pk)
    if request.method == 'POST':
        form = EditerForm(request.POST, request.FILES, instance=membre)
        if form.is_valid():
            nom = form.cleaned_data.get('last_name')
            prenom = form.cleaned_data.get('first_name')
            messages.success(request, f"Modification réusie avec succès au membre { nom } { prenom }.")
            form.save()
            return redirect('admin')
    else:
        form = EditerForm(instance=membre)
    return render(request, 'compte/editer.html', {'form':form, 'membre':membre})

# Page de supresion d'un membre.
@user_passes_test(administrateur, login_url='connecte')
def suprimerPage(request): 
    return render(request, 'compte/suprimer.html')

# Page de profile d'un membre (utilisateur).
@login_required(login_url='connecte')
def profilePage(request): 
    membre = request.user # Idendification du membre connecté.
    effectif = Membre.objects.all().count() # L'effectif des membre.
    # La somme payée et impayée de chaque cotisation d'un membre.
    payer_adhesion = MonAdhesion.objects.filter(membre=membre, paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_adhesion = MonAdhesion.objects.filter(membre=membre, paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_mensuel = Mensuel.objects.filter(membre=membre, paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_mensuel = Mensuel.objects.filter(membre=membre, paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_naissance = NouveauNe.objects.filter(membre=membre, paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_naissance = NouveauNe.objects.filter(membre=membre, paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_rejouissance = Rejouissance.objects.filter(membre=membre, paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_rejouissance = Rejouissance.objects.filter(membre=membre, paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_don = Don.objects.filter(membre=membre, paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_don = Don.objects.filter(membre=membre, paye=False).aggregate(Sum('montant'))['montant__sum']
    payer_deces = Deces.objects.filter(membre=membre, paye=True).aggregate(Sum('montant'))['montant__sum']
    impayer_deces = Deces.objects.filter(membre=membre, paye=False).aggregate(Sum('montant'))['montant__sum']
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
    # Total payé et impayé de chaque membre.
    total_paye = payer_adhesion + payer_mensuel + payer_naissance + payer_rejouissance + payer_don + payer_deces
    total_impaye = impayer_adhesion + impayer_mensuel + impayer_naissance + impayer_rejouissance + impayer_don + impayer_deces
    return render(request, 'compte/profile.html', {
        'effectif':effectif, 
        'payer_adhesion':payer_adhesion, 
        'impayer_adhesion':impayer_adhesion, 
        'payer_mensuel':payer_mensuel, 
        'impayer_mensuel':impayer_mensuel, 
        'payer_naissance':payer_naissance, 
        'impayer_naissance':impayer_naissance, 
        'payer_rejouissance':payer_rejouissance, 
        'impayer_rejouissance':impayer_rejouissance, 
        'payer_don':payer_don, 
        'impayer_don':impayer_don, 
        'payer_deces':payer_deces, 
        'impayer_deces':impayer_deces,
        'total_paye':total_paye, 
        'total_impaye':total_impaye, 
        'title':'Profil membre'
        })

# Page de mon profil.
@login_required(login_url='connecte')
def monprofilPage(request): 
    if request.method == 'POST':
        form = MotDePasseChangerForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important pour éviter de déconnecter l'utilisateur
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès!')
        else:
            messages.warning(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = MotDePasseChangerForm(request.user)
    return render(request, 'compte/mon_profil.html', {'form':form, 'title':'Mon profil'})

# Page d'aide.
@login_required(login_url='connecte')
def aidePage(request): # Page d'aide.
    return render(request, 'compte/aide.html', {'title':'Aide'})


# Réunion (Appel de présence).
@user_passes_test(administrateur, login_url='connecte')
def reunionPage(request): # Page de réunion.
    reunion = Reunion.objects.all()
    effectif = Membre.objects.all().count() # Effectif des membres.
    return render(request, 'reunion.html', {
        'reunion':reunion,
        'effectif':effectif,
        })

@user_passes_test(administrateur, login_url='connecte')
def reunion_ajouterPage(request): # Page pour ajouter la présence.
    if request.method  == 'POST':
        form = ReunionForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data.get('membre')
            form.save()
            messages.success(request, f"Appel créé avec succès pour { membre }")
            return redirect('reunion')
    else:
        form = ReunionForm()
    return render(request, 'reunion_ajouter.html', {'form':form})

@user_passes_test(administrateur, login_url='connecte')
def reunion_editerPage(request, pk): # Page de modification dùappel de présence.
    reunion = Reunion.objects.get(id=pk)
    if request.method  == 'POST':
        form = ReunionForm(request.POST, instance=reunion)
        if form.is_valid():
            form.save()
            messages.success(request, f"Appel de présence modifié avec succès {reunion.membre.last_name} {reunion.membre.first_name}")
            return redirect('reunion')
    else:
        form = ReunionForm(instance=reunion)
    return render(request, 'reunion_editer.html', {'form':form, 'reunion':reunion})