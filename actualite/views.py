# Imortation de modules.
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from compte.tests import administrateur
from .forms import ActualiteForm, CommentaireActiverForm, CommentaireForm
from .models import Actualite, Commentaire

# Création de pages webs.

def actualitePage(request): # Page d'actualité.
    actualite = Actualite.objects.all()
    reunion = Actualite.objects.filter(titre__icontains='réunion').count()
    naissance = Actualite.objects.filter(titre__icontains='naissance').count()
    rejouissance = Actualite.objects.filter(titre__icontains='rejouissance').count()
    don = Actualite.objects.filter(titre__icontains='don').count()
    deces = Actualite.objects.filter(titre__icontains='deces').count()
    derniers_articles = Actualite.objects.order_by('-date')[:5]
    return render(request, 'actualite/actualite.html', {
        'actualite':actualite, 
        'reunion':reunion, 
        'naissance':naissance, 
        'rejouissance':rejouissance, 
        'don':don, 'deces':deces, 
        'derniers_articles':derniers_articles, 
        'title':'Actualité'
        })

def detailPage(request, pk): # Page pour detailler les actualités.
    reunion = Actualite.objects.filter(titre__icontains='réunion').count()
    naissance = Actualite.objects.filter(titre__icontains='naissance').count()
    rejouissance = Actualite.objects.filter(titre__icontains='rejouissance').count()
    don = Actualite.objects.filter(titre__icontains='don').count()
    deces = Actualite.objects.filter(titre__icontains='deces').count()
    derniers_articles = Actualite.objects.order_by('-date')[:5]
    actualite = get_object_or_404(Actualite, pk=pk)
    comments = actualite.comments.filter(active=True)
    nombre = actualite.comments.filter(active=True).count()
    new_comment = None
    if request.method == 'POST':
        form = CommentaireForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.actualite = actualite
            new_comment.save()
    else:
        form = CommentaireForm()
    return render(request, 'actualite/detail.html', {
        'actualite': actualite, 
        'derniers_articles':derniers_articles, 
        'comments': comments, 
        'new_comment': new_comment, 
        'form': form, 'nombre':nombre, 
        'reunion':reunion, 
        'naissance':naissance, 
        'rejouissance':rejouissance, 
        'don':don, 
        'deces':deces,
        'title':'Actualité-détail'
        })

@user_passes_test(administrateur, login_url='connecte')
def actualite_listePage(request): # Page pour administrer les actualités.  
    actualite = Actualite.objects.all()
    return render(request, 'actualite/actualite_liste.html', {
        'actualite':actualite,
        'title':'Actualité ajoutée'
        })

@user_passes_test(administrateur, login_url='connecte')
def actualite_ajouterPage(request): # Page pour ajouter d'actualités.
    if request.method == "POST":
        form = ActualiteForm(request.POST, request.FILES)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            messages.success(request, f'Une nouvelle actualité titrée "{ titre }" a été ajouté.')
            form.save()
            return redirect('actualite_liste')
    else:
        form = ActualiteForm()
    return render(request, 'actualite/actualite_ajouter.html', {'form':form,'title':'Actualité ajoutée'})

@user_passes_test(administrateur, login_url='connecte')
def actualite_editerPage(request, pk): # Page pour éditer l'actualité.
    actualite = Actualite.objects.get(id=pk)
    if request.method == "POST":
        form = ActualiteForm(request.POST, request.FILES, instance=actualite)
        if form.is_valid():
            titre = form.cleaned_data.get('titre')
            messages.success(request, f"Modification réusie avec succès à l'actualité { titre }.")
            form.save()
            return redirect('actualite_liste')
    else:
        form = ActualiteForm(instance=actualite)
    return render(request, 'actualite/actualite_editer.html', {
        'form':form, 'actualite':actualite,
        'title':'Actualité ajoutée'
        })


@user_passes_test(administrateur, login_url='connecte')
def commentaire_listePage(request): # Page pour administrer les commentaires.  
    commentaire = Commentaire.objects.all()
    return render(request, 'actualite/commentaire_liste.html', {
        'commentaire':commentaire,
        'title':'Liste ommentaires'
        })

@user_passes_test(administrateur, login_url='connecte')
def commentaire_ajouterPage(request): # Page pour ajouter de commentaires.
    if request.method == "POST":
        form = CommentaireForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            messages.success(request, f'Un nouveau commentaire a été ajouté par { nom }.')
            form.save()
            return redirect('commentaire_liste')
    else:
        form = CommentaireForm()
    return render(request, 'actualite/commentaire_ajouter.html', {
        'form':form,
        'title':'Commentaire ajouté'
        })

@user_passes_test(administrateur, login_url='connecte')
def commentaire_editerPage(request, pk): # Page pour activer un commentaire.
    commentaire = Commentaire.objects.get(id=pk)
    if request.method == "POST":
        form = CommentaireActiverForm(request.POST, request.FILES, instance=commentaire)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            messages.success(request, f"Le commentaire de { nom } est activé avec succès.")
            form.save()
            return redirect('commentaire_liste')
    else:
        form = CommentaireActiverForm(instance=commentaire)
    return render(request, 'actualite/commentaire_editer.html', {
        'form':form, 'commentaire':commentaire, 
        'title':'Commentaire activé'
        })