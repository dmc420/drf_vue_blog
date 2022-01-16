from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    author = UserDescSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='article:detail')

    class Meta:
        model = Article
        fields = ['url', 'title', 'created', 'author']


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['author']
