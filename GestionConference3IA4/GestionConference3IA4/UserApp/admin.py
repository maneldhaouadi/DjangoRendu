from django.contrib import admin
from .models import User, OrganizingCommitee


# Personnalisation générale du dashboard admin

admin.site.site_header = "Conference Management Admin"
admin.site.site_title = "Conference Dashboard"
admin.site.index_title = "Gestion des utilisateurs et comités"


# Admin pour User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des utilisateurs
    list_display = ("user_id", "username", "first_name", "last_name", "email", "role", "affiliation", "nationality", "created_at")
    
    # Champs modifiables directement dans la liste
    list_editable = ("role", "affiliation", "nationality")
    
    # Filtres sur le côté
    list_filter = ("role", "affiliation", "nationality", "date_joined")
    
    # Barre de recherche
    search_fields = ("username", "first_name", "last_name", "email")
    
    # Sections du formulaire d’édition
    fieldsets = (
        ("Identité", {"fields": ("user_id", "username", "first_name", "last_name", "email")}),
        ("Informations supplémentaires", {"fields": ("affiliation", "nationality", "role")}),
        ("Dates", {"fields": ("date_joined", "last_login", "created_at", "updated_at")}),
    )
    
    # Champs non modifiables
    readonly_fields = ("user_id", "date_joined", "created_at", "updated_at", "last_login")


# Admin pour OrganizingCommitee

@admin.register(OrganizingCommitee)
class OrganizingCommiteeAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("user", "conference", "commitee_role", "date_join", "created_at")
    
    # Filtres sur le côté
    list_filter = ("commitee_role", "conference", "date_join")
    
    # Barre de recherche
    search_fields = ("user__username", "conference__name")
    
    # Sections du formulaire d’édition
    fieldsets = (
        ("Informations générales", {"fields": ("user", "conference", "commitee_role")}),
        ("Dates", {"fields": ("date_join", "created_at", "updated_at")}),
    )
    
    # Champs non modifiables
    readonly_fields = ("created_at", "updated_at")
