from django.db import models
from django.utils.translation import gettext_lazy as _

class Article (models.Model):
    """
    Modèle représentant un article.
    Attributs:
        title (str): Le titre de l'article, unique et limité à 50 caractères.
        content (str): Le contenu de l'article.
        publicationDate (datetime): La date et l'heure de publication de l'article.
    """
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    publicationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        représentation sous forme de chaîne de caractères de l'article.
        Returns:
            str: Le titre de l'article.
        """
        return self.title