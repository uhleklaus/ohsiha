from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

#def register(request):
 #   form = UserCreationForm()
  #  return render (request, 'userInput/register.html', {'form' : form})

def home(request):
    return render (request, 'userInput/home.html')

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('project-home')
    else:
        form = UserCreationForm()
    return render(request, 'userInput/register.html', {'form': form})