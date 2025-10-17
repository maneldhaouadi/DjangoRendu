from django.contrib import admin
from .models import *


admin.site.site_header = "Conference Management admin 25/26"
admin.site.site_title = "Conference dashboard"
admin.site.index_title = "Conference management"

class SubmissionStackedInline(admin.StackedInline):
    model = Submission
    extra = 1
    readonly_fields = ("submission_id", "submission_date")

class SubmissionTabularInline(admin.TabularInline):
    model = Submission
    extra = 1
    readonly_fields = ("submission_id", "submission_date")
    fields = ("title", "status", "user", "payed")


@admin.register(Conference)
class AdminPerso(admin.ModelAdmin):
    list_display = ("name", "theme", "location", "start_date", "end_date", "duration")
    ordering = ("start_date",)
    list_filter = ("theme", "location", "start_date")
    search_fields = ("name", "description", "location")
    fieldsets = (
        ("Information General", {
            "fields": ("conference_id", "name", "theme", "description")
        }),
        ("Logistics", {
            "fields": ("location", "start_date", "end_date")
        }),
    )
    readonly_fields = ("conference_id",)
    date_hierarchy = "start_date"
    inlines = [SubmissionStackedInline]

    def duration(self, objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date - objet.start_date).days
        return "RAS"
    duration.short_description = "Duration (days)"


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "user", "conference", "submission_date", "payed", "short_abstract")
    list_editable = ("status", "payed")
    list_filter = ("status", "payed", "conference", "submission_date")
    search_fields = ("title", "keywords", "user__username")

    fieldsets = (
        ("Infos générales", {
            "fields": ("submission_id", "title", "abstract", "keywords")
        }),
        ("Fichier et conférence", {
            "fields": ("paper", "conference")
        }),
        ("Suivi", {
            "fields": ("status", "payed", "submission_date", "user")
        }),
    )
    readonly_fields = ("submission_id", "submission_date")

    def short_abstract(self, obj):
        return obj.abstract[:50] + ("..." if len(obj.abstract) > 50 else "")
    short_abstract.short_description = "Abstract (short)"

 
    actions = ["mark_as_payed", "accept_submissions"]

    def mark_as_payed(self, request, queryset):
        updated = queryset.update(payed=True)
        self.message_user(request, f"{updated} soumissions marquées comme payées")
    mark_as_payed.short_description = "Marquer comme payées"

    def accept_submissions(self, request, queryset):
        updated = queryset.update(status="accepted")
        self.message_user(request, f"{updated} soumissions acceptées")
    accept_submissions.short_description = "Accepter les soumissions"
