# Importation de modules.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import Profile

# Affichage de tables models.
class MembreAdmin(UserAdmin):
    """
    Définissez le modèle d'administrateur pour le modèle d'utilisateur personnalisé sans champ 
    de nom d'utilisateur.
    """
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (('Personal info'), {'fields': (  
            'last_name',
            'first_name', 

            'contact',
            'ville',
            'quartier',
            'profession',
            'naissance',
            'photo',
            'adhesion',
            )}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'last_name',
                'first_name', 
                'email',

                'contact',
                'ville',
                'quartier',
                'profession',
                'naissance',
                'photo',
                'adhesion', 
                
                'password1', 
                'password2',
                ),
        }),
    )
    list_display = (
        'id',
        'last_name',
        'first_name', 
        'email',
        'contact',
        'ville',
        'quartier',
        'profession',
        'naissance',
        'photo',
        'adhesion',

        'is_staff',
        )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Enrégistrement de models.
admin.site.register(get_user_model(), MembreAdmin)
admin.site.register(Profile)