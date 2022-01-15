from django.shortcuts import render

from django.http import JsonResponse
from article.models import Article
# 这个 ArticleListSerializer 暂时还没有
from article.serializers import ArticleListSerializer


def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)
