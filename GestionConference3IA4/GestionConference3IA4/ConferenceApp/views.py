from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Conference, Submission, generate_submission_id
from .forms import ConferenceModel, SubmissionForm



def all_conference(request):
    conferences = Conference.objects.all()
    return render(request, 'conference/listConference.html', {'conferences': conferences})

class ConferenceList(LoginRequiredMixin, ListView):
    model = Conference
    context_object_name = "conferences"
    ordering = ['start_date']
    template_name = 'conference/listConference.html'
    login_url = 'login'

class ConferenceDetails(LoginRequiredMixin, DetailView):
    model = Conference
    context_object_name = "conference"
    template_name = 'conference/conference-details.html'
    login_url = 'login'

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

class ConferenceDelete(LoginRequiredMixin, DeleteView):
    model = Conference
    template_name = 'conference/Conference_confirm_delete.html'
    fields = "__all__"
    success_url = reverse_lazy("all_conference")
    login_url = 'login'



class ListSubmissions(LoginRequiredMixin, ListView):
    model = Submission
    context_object_name = "submissions"
    template_name = "submission/list_submission.html"
    login_url = 'login'

def get_queryset(self):
    return Submission.objects.filter(user=self.request.user)

class DetailSubmission(LoginRequiredMixin, DetailView):
    model = Submission
    context_object_name = "submission"
    template_name = "submission/detail_submission.html"
    login_url = 'login'

class AddSubmission(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "submission/add_submission.html"
    success_url = reverse_lazy("list_submission")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        if not form.instance.submission_id:
            form.instance.submission_id = generate_submission_id()
        return super().form_valid(form)



class UpdateSubmission(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "submission/add_submission.html"
    success_url = reverse_lazy("list_submission")
    login_url = 'login'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['conference'].disabled = True
        return form

    def test_func(self):
        submission = self.get_object()
        return submission.status not in ["accepted", "rejected"] and submission.user == self.request.user

