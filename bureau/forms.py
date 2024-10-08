# Importation de modules.
from django import forms

from .models import Bureau, Contact, Diaporama, Election, Ensemble, Galerie

# Formulaire du model actualité
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


# Formulaire de photo d'ensemble du bureau
class EnsembleForm(forms.ModelForm):
    
    class Meta:
        model = Ensemble
        fields = '__all__'
        widgets= {     
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


# Formulaire du model des élections.
class ElectionForm(forms.ModelForm):
    
    class Meta:
        model = Election
        fields = '__all__'
        widgets= {
            # président.
            'president': forms.NumberInput(
                attrs={
                    'id': 'president',
                    'class': 'form-control',  
                }
            ),

            # Sécrétaire.
            'secretaire': forms.NumberInput(
                attrs={
                    'id': 'secretaire',
                    'class': 'form-control',  
                }
            ),

            # Sécrétaire Adjoint.
            'secretaire_adjoint': forms.NumberInput(
                attrs={
                    'id': 'secretaire_adjoint',
                    'class': 'form-control',  
                }
            ),
            
            # Trésorier.
            'tresorier': forms.NumberInput(
                attrs={
                    'id': 'tresorier',
                    'class': 'form-control',  
                }
            ),

            # Trésorier Adjoint.
            'tresorier_adjoint': forms.NumberInput(
                attrs={
                    'id': 'tresorier_adjoint',
                    'class': 'form-control',  
                }
            ),

            # Conseiller.
            'conseiller_1': forms.NumberInput(
                attrs={
                    'id': 'conseiller_1',
                    'class': 'form-control',  
                }
            ),

            # Conseiller.
            'conseiller_2': forms.NumberInput(
                attrs={
                    'id': 'conseiller_2',
                    'class': 'form-control',  
                }
            ),
        }


# Formulaire du model galerie.
class GalerieForm(forms.ModelForm):
    
    class Meta:
        model = Galerie
        fields = '__all__'
        widgets= {
            # Titre.
            'titre': forms.Select(
                attrs={
                    'id': 'titre',
                    'class': 'form-control',  
                }
            ),

            # Intitulé.
            'intitule': forms.TextInput(
                attrs={
                    'id': 'intitule',
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


# Formulaire du model diaporama.
class DiaporamaForm(forms.ModelForm):
    
    class Meta:
        model = Diaporama
        fields = '__all__'
        widgets= {
            # Titre.
            'titre': forms.Select(
                attrs={
                    'id': 'titre',
                    'class': 'form-control',  
                }
            ),

            # Intitulé.
            'intitule': forms.TextInput(
                attrs={
                    'id': 'intitule',
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


# Formulaire du model Contact.
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets= {
            # nom.
            'nom': forms.TextInput(
                attrs={
                    'id': 'nom',
                    'class': 'form-control',
                    'placeholder': 'Nom'  
                }
            ),

            # prenom.
            'prenom': forms.TextInput(
                attrs={
                    'id': 'prenom',
                    'class': 'form-control',
                    'placeholder': 'Prénom'  
                }
            ),

            # Email.
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'class': 'form-control',  
                    'placeholder': 'Email'
                }
            ),

            # Sujet.
            'sujet': forms.TextInput(
                attrs={
                    'id': 'sujet',
                    'class': 'form-control',  
                    'placeholder': 'Sujet'
                }
            ),

            # Message.
            'message': forms.Textarea(
                attrs={
                    'id': 'message',
                    'class': 'form-control', 
                    'placeholder': 'Message', 
                    'rows' : '3' 
                }
            ),            
        }