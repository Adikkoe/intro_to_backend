# blog/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Article

def article_list(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False)

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return JsonResponse({
        'title': article.title,
        'text': article.text,
        'author': article.author
    })
