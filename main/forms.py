from django import forms
from .models import Article

class ArticleCreate(forms.ModelForm):
    """
     Formulaire pour créer un nouvel article.
     il utilise le modèle `Article` et inclut les champs 'title' et 'content'.
    """
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control rounded-3',
                'id': 'floatingInput',
                'placeholder': '{% trans "Titre" %}'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control rounded-3',
                'id': 'floatingPassword',
                'placeholder': '{% trans "Contenu" %}',
            }),
        }