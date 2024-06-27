from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# from openai import OpenAI, RateLimitError
# from .forms import ArticleCreate
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
