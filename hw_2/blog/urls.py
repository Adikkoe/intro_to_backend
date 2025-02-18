# blog/views.py
from django.shortcuts import render
from .models import Article
from django.http import JsonResponse

def article_list(request):
    articles = Article.objects.all()
    article_data = [{"title": article.title, "text": article.text, "author": article.author} for article in articles]
    return JsonResponse(article_data, safe=False)

def article_detail(request, id):
    article = Article.objects.get(id=id)
    article_data = {"title": article.title, "text": article.text, "author": article.author}
    return JsonResponse(article_data)
