from django.contrib import admin
from .models import Session

# =========================
# Personnalisation de l'admin pour Session
# =========================
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("session_id", "title", "topic", "conference", "session_day", "start_time", "end_time", "room", "created_at")
    
    # Champs modifiables directement dans la liste (facultatif)
    list_editable = ("start_time", "end_time", "room")
    
    # Filtres sur le côté
    list_filter = ("conference", "session_day", "room", "topic")
    
    # Barre de recherche
    search_fields = ("title", "topic", "room", "conference__name")
    
    # Structure du formulaire
    fieldsets = (
        ("Informations générales", {
            "fields": ("title", "topic", "conference", "room")
        }),
        ("Horaires", {
            "fields": ("session_day", "start_time", "end_time")
        }),
        ("Dates de suivi", {
            "fields": ("created_at", "updated_at")
        }),
    )
    
    # Champs en lecture seule
    readonly_fields = ("created_at", "updated_at")
