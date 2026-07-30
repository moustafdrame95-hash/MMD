
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def accueil(request): 
    return HttpResponse("<p>Bienvenue sur ma page capteurs<p\>")