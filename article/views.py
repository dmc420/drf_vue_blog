from django.http import HttpResponse
from rest_framework import viewsets, filters

from article.models import Article
from article.serializers import ArticleSerializer
from article.permissions import IsAdminUserOrReadOnly


def index(request):
    return HttpResponse('Hello World!')


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
