from django.contrib.auth.forms import UserCreationForm
from django import forms
from  .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "email", "role", "affiliation", "nationality", "password1", "password2"]
        widgets = {
            "email": forms.EmailInput(),
            "password1": forms.PasswordInput(),
            "password2": forms.PasswordInput(),
        }
