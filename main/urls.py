from django.urls import path
from .views import index, create_article, chatbot

urlpatterns = [
    path('', index, name="main-index"),
    path('create/', create_article, name="main-create"),
    path('chatbot/', chatbot, name="main-chat"),
]