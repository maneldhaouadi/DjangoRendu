from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib.auth import logout


# Create your views here.
#creation une fonction personnalise
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form}) 

def logout_view(req):
    logout(req)
    return redirect("login")
