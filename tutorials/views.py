from django.shortcuts import render, redirect
from .forms import TutorialForm
from .models import Tutorial
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'tutorial/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'tutorial/signin.html', {'form': form})

@login_required
def tutorialList(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/list.html', { 'tutorials' : tutorials})


def home(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/home.html', { 'tutorials' : tutorials})    

@login_required
def uploadTutorial(request):
    if request.method == 'POST':  
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial/upload.html', {'form' : form})

@login_required
def deleteTutorial(request, pk):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete()
    return redirect('tutorial_list')

def signout(request):
    logout(request)
    return redirect('/')