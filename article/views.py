from django.http import HttpResponse
from rest_framework import viewsets, filters

from article.models import Article, Category, Tag
from article.serializers import (ArticleSerializer, ArticleDetailSerializer,
                                 CategorySerializer, CategoryDetailSerializer,
                                 TagSerializer)
from article.permissions import IsAdminUserOrReadOnly


def index(request):
    return HttpResponse('Hello World!')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    分类视图集
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章视图集
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
