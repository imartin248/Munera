from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from . import models

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('giftlist:home')

    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('giftlist:home')
