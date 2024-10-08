from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


from bureau.forms import DiaporamaForm, GalerieForm, ContactForm
from bureau.models import Contact, Diaporama, Galerie
from compte.models import Membre # Importation du model membre.
from compte.tests import administrateur

# CREATION DE PAGES (VUES)

# Page d'accueil.
def accueilPage(request): 
    effectif = Membre.objects.all().count() # L'effectif des membre.
    galerie = Galerie.objects.all()
    diaporama = Diaporama.objects.all()
    return render(request, 'index.html', {
        'effectif':effectif, 
        'galerie':galerie, 
        'diaporama':diaporama, 
        'title':'Accueil'
        })

# Page de contact de l'AJRDL.
def contactPage(request): 
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            messages.success(request, f"le message de { nom } { prenom } a été envoyé. Merci !")
            form.save()
            return redirect('contact')
        form = ContactForm()    
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'title':'Contact'})

# Page de membres.
def membrePage(request): 
    membre = Membre.objects.all() # Récupérqtion de tous les membre.
    return render(request, 'membre.html', {
        'membre':membre, 'title':'Espace membre'
        })

# Page de règlements intérieurs.
def reglementPage(request): 
    return render(request, 'reglement.html', {'title':'Règlement'})

# Page de statut.
def statutPage(request): 
    return render(request, 'statut.html', {'title':'Statut'})

# Page de projets.
def projetPage(request): 
    return render(request, 'projet.html', {'title':'Projets'})

# Page de visions.
def visionPage(request): 
    return render(request, 'vision.html', {'title':'Vision'})

# Page d'information.
def informationPage(request): 
    return render(request, 'information.html', {'title':'Information'})

# Page de réalisation.
def realisationPage(request): 
    return render(request, 'realisation.html', {'title':'Réalisation'}) 

# Page de Galerie.
@user_passes_test(administrateur, login_url='connecte')
def galerie_listePage(request): # Page pour administrer les galeries.  
    galerie = Galerie.objects.all()
    return render(request, 'galerie_liste.html', {
        'galerie':galerie, 'title':'Liste bureau'
        })

@user_passes_test(administrateur, login_url='connecte')
def galerie_ajouterPage(request): # Page pour ajouter une galerie.
    if request.method == "POST":
        form = GalerieForm(request.POST, request.FILES)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            intitule = form.cleaned_data.get('intitule')
            messages.success(request, f"Galerie { titre } { intitule } a été ajoutée.")
            form.save()
            return redirect('galerie')
    else:
        form = GalerieForm()
    return render(request, 'galerie_ajouter.html', {
        'form':form,'title':'Ajouter galerie'
        })

@user_passes_test(administrateur, login_url='connecte')
def galerie_editerPage(request, pk): # Page pour éditer une galerie.
    galerie = Galerie.objects.get(id=pk)
    if request.method == "POST":
        form = GalerieForm(request.POST, request.FILES, instance=galerie)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            intitule = form.cleaned_data.get('intitule')
            messages.success(request, f"Galerie { titre } { intitule } modifiée.")
            form.save()
            return redirect('galerie')
    else:
        form = GalerieForm(instance=galerie)
    return render(request, 'galerie_editer.html', {
        'form':form, 
        'galerie':galerie, 
        'title':'Editer galerie'
        })


# Page de Diaporama.
@user_passes_test(administrateur, login_url='connecte')
def diaporama_listePage(request): # Page pour administrer les diaporamas.  
    diaporama = Diaporama.objects.all()
    return render(request, 'diaporama_liste.html', {
        'diaporama':diaporama, 
        'title':'Liste Diaporama'
        })

@user_passes_test(administrateur, login_url='connecte')
def diaporama_ajouterPage(request): # Page pour ajouter un diaporama.
    if request.method == "POST":
        form = DiaporamaForm(request.POST, request.FILES)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            intitule = form.cleaned_data.get('intitule')
            messages.success(request, f"Diaporama { titre } { intitule } a été ajouté.")
            form.save()
            return redirect('diaporama')
    else:
        form = DiaporamaForm()
    return render(request, 'diaporama_ajouter.html', {
        'form':form, 
        'title':'Ajouter diaporama'
        })

@user_passes_test(administrateur, login_url='connecte')
def diaporama_editerPage(request, pk): # Page pour éditer une galerie.
    diaporama = Diaporama.objects.get(id=pk)
    if request.method == "POST":
        form = DiaporamaForm(request.POST, request.FILES, instance=diaporama)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            intitule = form.cleaned_data.get('intitule')
            messages.success(request, f"Diaporama { titre } { intitule } modifiée.")
            form.save()
            return redirect('diaporama')
    else:
        form = GalerieForm(instance=diaporama)
    return render(request, 'diaporama_editer.html', {
        'form':form, 
        'galerie':diaporama, 
        'title':'Editer diaporama'
        })


# Page de Contact.
@user_passes_test(administrateur, login_url='connecte')
def contact_listePage(request): # Page pour administrer les contacts.  
    contact = Contact.objects.all()
    return render(request, 'contact_liste.html', {
        'contact':contact, 
        'title':'Liste Contact'
        })

@user_passes_test(administrateur, login_url='connecte')
def contact_detailPage(request, pk): # Page pour plus de détail sur le contact.
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():        
            form.save()
            return redirect('contact_liste')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_detail.html', {
        'form': form, 
        'contact': contact, 
        'title': 'Contact détail'
        })

@user_passes_test(administrateur, login_url='connecte')
def contact_suprimerPage(request, pk): # Page pour suprimer un contact.  
    if request.method == "POST":
        contact = get_object_or_404(Contact, id=pk)  
        contact.delete()
        return redirect('contact_liste')   
    return render(request, 'contact_suprimer.html', {'title': 'Editer diaporama'})