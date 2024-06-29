from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def set_language(request, language):
    """
    Modifie la langue actuelle de l'application en fonction de la langue spécifiée dans la requête.

    Cette fonction résoud la vue correspondant à l'URL de la page précédente pour rediriger
    l'utilisateur vers la même page après avoir changé la langue. Si la vue ne peut pas être résolue,
    l'utilisateur est redirigé vers la page d'accueil.
    Args:
        request (HttpRequest): L'objet requête HTTP.
        language (str): Le code de la langue à laquelle passer (par exemple, 'fr' pour français).
    Returns:
        HttpResponseRedirect: Une réponse de redirection vers l'URL de la vue résolue ou vers la page d'accueil.
    """
    view = None
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:  # resolution de la vue correspondant à l’URL de la page précédente
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
