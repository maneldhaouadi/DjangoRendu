from django import forms
from .models import Conference, Submission

class ConferenceModel(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'theme', 'description', 'location', 'start_date', 'end_date']  
        labels = {
            'name': "Nom de la conférence",
            'theme': "Thème de la conférence",
            'description': 'Description',
            'location': 'Lieu de la conférence',
            'start_date': 'Date de début',
            'end_date': "Date de fin"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Ex : Conférence 3IA4"
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': "Date de début"
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': "Date de fin"
                }
            ),
        }

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['conference', 'title', 'abstract', 'keywords', 'paper', 'status', 'payed']
        labels = {
            'conference': 'Conférence',
            'title': 'Titre',
            'abstract': 'Résumé',
            'keywords': 'Mots-clés',
            'paper': 'Fichier PDF',
            'status': 'Statut',
            'payed': 'Paiement effectué'
        }
        widgets = {
            'abstract': forms.Textarea(attrs={'rows': 5}),
            'keywords': forms.TextInput(attrs={'placeholder': 'ex: IA, Big Data, Cloud'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'payed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
