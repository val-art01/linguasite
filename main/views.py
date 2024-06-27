from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# from openai import OpenAI, RateLimitError
from .forms import ArticleCreate
from .models import Article
from django.conf import settings

def index(request):
    """
    Affiche la page d'accueil avec la liste des articles recuprer dans la base de données
    Args:
        request (HttpRequest): L'objet de requête HTTP.
    Returns:
        HttpResponse: La réponse HTTP avec le template rendu contenant la liste des
    """
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})

def create_article(request):
    """
    gere l'ajout d'un nouvel article par le visiteur via un formulaire.
    en verifiant si la requête est de type POST et que les champs sont valident
    Args:
        request (HttpRequest): L'objet de requête HTTP.
    Returns:
        HttpResponse: La réponse HTTP avec le formulaire rendu dans le template 'add_article.html'.
    """
    if request.method == 'POST':
        form = ArticleCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = ArticleCreate()
    return render(request, 'main/create_article.html', {'form': form})
