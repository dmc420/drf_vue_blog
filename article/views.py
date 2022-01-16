from django.http import HttpResponse
from rest_framework import viewsets

from article.models import Article
from article.serializers import ArticleSerializer
from article.permissions import IsAdminUserOrReadOnly


def index(request):
    return HttpResponse('Hello World!')


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
