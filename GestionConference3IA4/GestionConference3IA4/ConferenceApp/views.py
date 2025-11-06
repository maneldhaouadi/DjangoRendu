from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Conference
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ConferenceModel
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def all_conference(req):
    conferences=Conference.objects.all()
    return render(req,'conference/listConference.html',{'conferences':conferences})
# Create your views here.

#hne lezmk t7out nafs l esm     context_object_name="conferences"

class ConferenceList(ListView):
    model= Conference
    context_object_name="conferences"
    ordering=['start_date']
    template_name='conference/listConference.html'

class ConferenceDetails(DetailView):
     model= Conference
     context_object_name="conference"
     template_name='conference/conference-details.html'

class ConferenceCreate(LoginRequiredMixin, CreateView):
    model = Conference
    template_name = 'conference/Conference_form.html'
    form_class = ConferenceModel
    success_url = reverse_lazy('all_conference')
    login_url = 'login'

class ConferenceUpdate(LoginRequiredMixin, UpdateView):
    model = Conference
    template_name = 'conference/Conference_form.html'
    form_class = ConferenceModel
    success_url = reverse_lazy('all_conference')
    login_url = 'login'

class ConferenceDelete(LoginRequiredMixin,DeleteView):
    model=Conference
    template_name='conference/Conference_confirm_delete.html'
    fields="__all__"
    success_url=reverse_lazy("all_conference")

