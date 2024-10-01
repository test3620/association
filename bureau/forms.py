# Importation de modules.
from django import forms

from .models import Bureau

# Récupération de tables du model actualité
class BureauForm(forms.ModelForm):
    
    class Meta:
        model = Bureau
        fields = '__all__'
        widgets= {
            # Nom.
            'nom': forms.TextInput(
                attrs={
                    'id': 'nom',
                    'class': 'form-control',  
                }
            ),

            # Prénom.
            'prenom': forms.TextInput(
                attrs={
                    'id': 'prenom',
                    'class': 'form-control',  
                }
            ),

            # Titre.
            'titre': forms.TextInput(
                attrs={
                    'id': 'titre',
                    'class': 'form-control',  
                }
            ),
            
            # Photo.
            'photo': forms.FileInput(
                attrs={
                    'id': 'photo',
                    'class': 'form-control',   
                }
            ),
        }