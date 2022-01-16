from rest_framework import serializers
from article.models import Article, Category
from user_info.serializers import UserDescSerializer


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    @staticmethod
    def validate_category_id(value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError('Category with id {} not exists.'.format(value))
        return value

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """
    给分类详情的嵌套序列化器
    """
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title'
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """
    分类详情
    """
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]
