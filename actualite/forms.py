# Importation de modules.
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Actualite, Commentaire

# Formulaire d'actualité.
class ActualiteForm(forms.ModelForm):
    
    class Meta:
        model = Actualite
        fields = ['titre', 'contenu', 'auteur', 'image']
        widgets= {
            # Titre.
            'titre': forms.TextInput(
                attrs={
                    'id': 'titre',
                    'class': 'form-control',  
                }
            ),

            # Contenu.
            'contenu': SummernoteWidget(),

            # Auteur.
            'auteur': forms.Select(
                attrs={
                    'id': 'auteur',
                    'class': 'form-control',
                }
            ),

            # Date.
            'date': forms.DateTimeInput(
                attrs={
                    'id': 'date',
                    'class': 'form-control',
                }
            ),
            
            # Image.
            'image': forms.FileInput(
                attrs={
                    'id': 'image',
                    'class': 'form-control',   
                }
            ),
        }

# Formulaire du commentaire.
class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('nom', 'contenu')
        widgets= {
            # Nom.
            'nom': forms.TextInput(
                attrs={
                    'id': 'nom',
                    'class': 'form-control',
                    'placeholder': 'Nom / Prénom' 
                }
            ),

            # Contenu.
            'contenu': forms.Textarea(
                attrs={
                    'id': 'contenu',
                    'class': 'form-control',
                    'placeholder': 'Messages',
                    'rows': '2'
                }
            )
        }

# Formulaire pour activer un commentaire.
class CommentaireActiverForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('nom', 'contenu', 'actualite', 'active')
        widgets= {

            # Actualité.
            'actualite': forms.Select(
                attrs={
                    'id': 'actualite',
                    'class': 'form-control',
                }
            ),

            # Nom.
            'nom': forms.TextInput(
                attrs={
                    'id': 'nom',
                    'class': 'form-control',
                    'placeholder': 'Nom / Prénom' 
                }
            ),

            # Contenu.
            'contenu': forms.Textarea(
                attrs={
                    'id': 'contenu',
                    'class': 'form-control',
                    'placeholder': 'Messages',
                    'rows': '2'
                }
            ),

        # Activer.
            'active': forms.CheckboxInput(
                attrs={
                    'id': 'active',
                }
            )
        }