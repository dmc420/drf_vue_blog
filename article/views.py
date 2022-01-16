from rest_framework import generics

from article.models import Article
from article.serializers import ArticleListSerializer, ArticleDetailSerializer
from article.permissions import IsAdminUserOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    """
    文章列表视图
    """
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    文章详情视图
    """
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
