from django.urls import path
from .views import index, create_article

urlpatterns = [
    path('', index, name="main-index"),
    path('create/', create_article, name="main-create"),
    # path('chatbot/', chat, name="main-chat"),
]