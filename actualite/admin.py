from django.contrib import admin

from .models import Actualite, Commentaire

# Affichage du model en table.

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contenu', 'actualite', 'date')
    list_filter = ('active', 'date')
    search_fields = ('nom', 'email', 'contenu')
    actions = ['approve_comments']

    def approve_commentaire(self, request, queryset):
        queryset.update(active=True)

# Enrégistrement de models.
admin.site.register(Actualite)
admin.site.register(Commentaire, CommentaireAdmin)