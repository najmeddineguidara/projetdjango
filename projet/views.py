from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ArtyProd.forms import DemandeProjetForm
@login_required
def home(request):
     context={'val':"Menu Acceuil"}
     return render(request,'home.html',context)
def about(request):
    return render(request, 'about.html')
