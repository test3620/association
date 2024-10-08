# Importation de modules
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth import get_user_model
from django import forms

from .models import Profile


# Formulaire pour l'inscription d'un membre.
class MembreForm(UserCreationForm): # Formulaire personnalisé d'utilisateur.
    """Un formulaire personnalisé pour créer de nouveaux membres."""

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'            
            }),
    )
    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmation' 
            }),
    ) 

    class Meta:
        model = get_user_model()
        fields = ['email', 'last_name','first_name', 'ville', 'quartier', 'profession', 'contact', 'naissance','photo','password1', 'password2']
        widgets = {  # Widgets des champs du model 'Membre'
         # Nom
         'last_name': forms.TextInput(
            attrs={
                'id': 'last_name',
                'class': 'form-control',
                'placeholder': 'Nom'
            }
         ),

         # Prénom
         'first_name': forms.TextInput(
            attrs={
                'id': 'first_name',
                'class': 'form-control',
                'placeholder': 'Prénom'
            }
         ),

         # Profession
         'profession': forms.TextInput(
            attrs={
                'id': 'profession',
                'class': 'form-control',
                'placeholder': 'Profession'
            }
         ),

         # Email
         'email': forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'Email'
            }
         ),
         
         # Ville résidentielle
         'ville': forms.TextInput(
            attrs={
                'id': 'ville',
                'class': 'form-control',
                'placeholder': 'Ville habitée'
            }
         ),

         # Quartier
         'quartier': forms.TextInput(
            attrs={
                'id': 'quartier',
                'class': 'form-control',
                'placeholder': 'Quartier'
            }
         ),

         # Contact
         'contact': PhoneNumberPrefixWidget( 
            initial="TG",
            attrs={
                'id': 'contact',
                'class': 'form-control flex-fill',
                'placeholder': '90000000'
            }
         ),

         # Date de naissance
         'naissance': forms.SelectDateWidget(
            years=(1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024),
            attrs={
                'id': 'naissance',
                'class':'form-control'
            }
         ),

         # Photo d'identité
         'photo': forms.FileInput(
            attrs={
                'id': 'photo',
                'class': 'form-control',
                'placeholder': "Photo"
            }
         ),

         # Date d'adhésion
         'adhesion': forms.SelectDateWidget(
            attrs={        
                'class': 'form-control',
            }
         ),
      }


# Formulaire de  modification d'informations  d'un utilisateur.
class EditerForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'last_name','first_name', 'ville', 'quartier', 'profession', 'contact', 'naissance','photo', 'is_active', 'is_staff', 'password']
        widgets = {
         # Nom
         'last_name': forms.TextInput(
            attrs={
                'id': 'last_name',
                'class': 'form-control d-flex',
                'placeholder': 'Nom'
            }
         ),

         # Prénom
         'first_name': forms.TextInput(
            attrs={
                'id': 'first_name',
                'class': 'form-control',
                'placeholder': 'Prénom'
            }
         ),

         # Profession
         'profession': forms.TextInput(
            attrs={
                'id': 'profession',
                'class': 'form-control',
                'placeholder': 'Profession'
            }
         ),

         # Email
         'email': forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'Email'
            }
         ),
         
         # Ville résidentielle
         'ville': forms.TextInput(
            attrs={
                'id': 'ville',
                'class': 'form-control',
                'placeholder': 'Ville habitée'
            }
         ),

         # Quartier
         'quartier': forms.TextInput(
            attrs={
                'id': 'quartier',
                'class': 'form-control',
                'placeholder': 'Quartier'
            }
         ),

         # Contact
         'contact': PhoneNumberPrefixWidget( 
            initial="TG",
            attrs={
                'id': 'contact',
                'class': 'form-control flex-fill',
            }
         ),

         # Date de naissance
         'naissance': forms.SelectDateWidget(
            years=(1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024),
            attrs={
                'id': 'naissance',
                'class':'form-control'
            }
         ),

         # Photo d'identité
         'photo': forms.FileInput(
            attrs={
                'id': 'photo',
                'class': 'form-control',
                'type': 'file'
            }
         ),

         # Membre actif
         'is_active': forms.CheckboxInput(
            attrs={
                'id': 'membre'
            }
         ),

         # Administrateur
         'is_staff': forms.CheckboxInput(
            attrs={
                'id': 'admin',
            }
         ),
      }


# Formulaire de modification du mot de passe.
class MotDePasseChangerForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Ancien'
            })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Nouveau'
            })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirmez'
            })


# Formulaire de modification d'image de profile.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image':forms.FileInput(
                attrs={
                    'id':'image',
                    'class':'form-control'
                }
            )
        }