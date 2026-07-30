from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .forms import ProduitForm

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'boutique/liste.html', {'produits': produits})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'boutique/detail.html', {'produit': produit})

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'boutique/formulaire.html', {'form': form, 'titre': 'Ajouter un produit'})

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('detail_produit', produit_id=produit.id)
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'boutique/formulaire.html', {'form': form, 'titre': 'Modifier le produit'})

def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'boutique/supprimer.html', {'produit': produit})