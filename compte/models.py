# Importation de modules.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image, ImageDraw, ImageFont


class CustomUserManager(BaseUserManager): # Gestionnaire d'utilisateur personnalisé.
    """
    Définissez un gestionnaire de modèles pour le modèle utilisateur sans champ de 
    nom d'utilisateur.
    """

    def _create_user(self, email, password=None, **extra_fields):
        """
        Créez et enregistrez un utilisateur avec l'e-mail et le mot de passe donnés.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Créez et enregistrez un superutilisateur avec l'e-mail et le mot de passe donnés.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Membre(AbstractUser): # Model d'utilisateur.
    username = None

    contact = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    naissance = models.DateField()
    photo = models.ImageField(upload_to='membre/identite/', height_field=None, width_field=None, max_length=None)
    adhesion = models.DateField(auto_now=False, auto_now_add=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"     
    
# model de profile.
class Profile(models.Model):
    membre = models.OneToOneField(Membre, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='membre/profile')

    def __str__(self): # Affichage par nom et prénom du membre.
        return f'{self.membre.last_name} {self.membre.first_name} Profile'

    