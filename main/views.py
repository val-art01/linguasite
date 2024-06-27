from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from openai import OpenAI, RateLimitError
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

def chatbot(request):
    """
    Gère les requêtes de chat pour interagir avec un modèle GPT-4 d'OpenAI.
    Cette fonction traite les requêtes POST contenant une question et envoie cette question à l'API
    OpenAI pour obtenir une réponse. Si la requête est réussie, elle retourne la réponse sous forme
    de JSON. En cas de surcharge de l'API ou d'autre erreur, elle retourne un message d'erreur approprié.
    Args:
        request (HttpRequest): L'objet de requête HTTP.
    Returns:
        JsonResponse: Une réponse JSON contenant la réponse du chatbot.
        HttpResponse: Une réponse HTTP contenant une page de chat ou un message d'erreur.
    Raises:
        RateLimitError: Si l'API OpenAI est surchargée.
        Exception: Pour toute autre erreur liée à l'API OpenAI.
    """
    client = OpenAI(api_key=settings.API_KEY)
    print(settings.API_KEY)
    if request.method == 'POST':
        question = request.POST.get('question')
        print(question)
        try:
            completion = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
                temperature=0.7,
                n=1,
                stop=None
            )
            print("aswer: ", completion)
            answer = completion.choices[0].message.content
            return JsonResponse({'answer': answer})
        except RateLimitError:
            error_message = "Désolé, le chatbot est actuellement surchargé. Veuillez réessayer plus tard."
            return render(request, 'main/chat.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"Erreur OpenAI : {e}"
            return JsonResponse({'error': str(error_message)}, status=500)
    return render(request, 'main/chat.html')
