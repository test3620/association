# Importation de modules.
from django import forms

from .models import Deces, Depense, Don, Entree, Mensuel, MonAdhesion, NouveauNe, Rejouissance, Reunion # Importation de models.


# Création de formulaire pour le mensuel.

# Formulaire de réunion.
class ReunionForm(forms.ModelForm):
    
    class Meta:
        model = Reunion
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control',  
                }
            ),

            # Réunion.
            'reunion': forms.TextInput(
                attrs={
                    'id': 'reunion',
                    'class': 'form-control',
                    'type' : 'date',
                }
            ),
            
            # Présence.
            'presence': forms.CheckboxInput(
                attrs={
                    'id': 'presence',
                }
            ),

            # retard.
            'retard': forms.CheckboxInput(
                attrs={
                    'id': 'retard',
                }
            ),

            # Permission.
            'permission': forms.CheckboxInput(
                attrs={
                    'id': 'permission',
                }
            ),

            # Absence.
            'absence': forms.CheckboxInput(
                attrs={
                    'id': 'absence',
                }
            ),
        }


# Formulaire d'adhésion.
class AdhesionForm(forms.ModelForm):
    
    class Meta:
        model = MonAdhesion
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control',  
                }
            ),

            # Réunion.
            'reunion': forms.TextInput(
                attrs={
                    'id': 'reunion',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Lieu.
            'lieu': forms.TextInput(
                attrs={
                    'id': 'lieu',
                    'class': 'form-control',
                }
            ),
            
            # Payer.
            'paye': forms.CheckboxInput(
                attrs={
                    'id': 'paye',
                }
            ),
        }


# Formulaire du mensuel.
class MensuelForm(forms.ModelForm):
    
    class Meta:
        model = Mensuel
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control',  
                }
            ),

            # Réunion.
            'reunion': forms.TextInput(
                attrs={
                    'id': 'reunion',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Lieu.
            'lieu': forms.TextInput(
                attrs={
                    'id': 'lieu',
                    'class': 'form-control',
                }
            ),
            
            # Payer.
            'paye': forms.CheckboxInput(
                attrs={
                    'id': 'paye',
                }
            ),
        }


# Formulaire de naissance.
class NaissanceForm(forms.ModelForm):
    
    class Meta:
        model = NouveauNe
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control',  
                }
            ),

            # Réunion.
            'reunion': forms.TextInput(
                attrs={
                    'id': 'reunion',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Enfant.
            'enfant': forms.TextInput(
                attrs={
                    'id': 'enfant',
                    'class': 'form-control',
                }
            ),
            
            # Payer.
            'paye': forms.CheckboxInput(
                attrs={
                    'id': 'paye',
                }
            ),
        }

# Formulaire de réjouissance.
class RejouissanceForm(forms.ModelForm):
    
    class Meta:
        model = Rejouissance
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control' 
                }
            ),

            # Date.
            'date': forms.TextInput(
                attrs={
                    'id': 'date',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Lieu.
            'lieu': forms.TextInput(
                attrs={
                    'id': 'lieu',
                    'class': 'form-control'
                }
            ),
            
            # Payer.
            'paye': forms.CheckboxInput(
                attrs={
                    'id': 'paye',
                }
            ),
        }

# Formulaire de don.
class DonForm(forms.ModelForm):
    
    class Meta:
        model = Don
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control',  
                }
            ),

            # Réunion.
            'reunion': forms.TextInput(
                attrs={
                    'id': 'reunion',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Objet.
            'objet': forms.TextInput(
                attrs={
                    'id': 'objet',
                    'class': 'form-control',
                }
            ),
            
            # Payer.
            'paye': forms.CheckboxInput(
                attrs={
                    'id': 'paye',
                }
            ),
        }

# Formulaire de décès.
class DecesForm(forms.ModelForm):
    
    class Meta:
        model = Deces
        fields = '__all__'
        widgets= {
            # Membre.
            'membre': forms.Select(
                attrs={
                    'id': 'membre',
                    'class': 'form-control',  
                }
            ),

            # Réunion.
            'reunion': forms.TextInput(
                attrs={
                    'id': 'reunion',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Enfant.
            'deces': forms.TextInput(
                attrs={
                    'id': 'deces',
                    'class': 'form-control',
                }
            ),
            
            # Payer.
            'paye': forms.CheckboxInput(
                attrs={
                    'id': 'paye',
                }
            ),
        }

# Formulaire des entrées.
class EntreeForm(forms.ModelForm):
    
    class Meta:
        model = Entree
        fields = '__all__'
        widgets= {        
            # Libellé.
            'libelle': forms.TextInput(
                attrs={
                    'id': 'lieu',
                    'class': 'form-control'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Date.
            'date': forms.TextInput(
                attrs={
                    'id': 'date',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),       
        }

# Formulaire de dépenses.
class DepenseForm(forms.ModelForm):
    
    class Meta:
        model = Depense
        fields = '__all__'
        widgets= {        
            # Libellé.
            'libelle': forms.TextInput(
                attrs={
                    'id': 'lieu',
                    'class': 'form-control'
                }
            ),

            # Montant.
            'montant': forms.TextInput(
                attrs={
                    'id': 'montant',
                    'class': 'form-control',
                    'type': 'number'
                }
            ),

            # Date.
            'date': forms.TextInput(
                attrs={
                    'id': 'date',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),       
        }