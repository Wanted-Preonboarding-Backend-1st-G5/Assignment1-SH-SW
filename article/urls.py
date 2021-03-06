from django.urls import path, include
from rest_framework.routers import SimpleRouter

from article.views import ArticleViewSet, CommentViewSet, CCommentViewSet, CategoryViewSet

app_name = 'article'

router = SimpleRouter()

router.register('articles', ArticleViewSet, basename='articles')
router.register('comments', CommentViewSet, basename='comments')
router.register('ccomments', CCommentViewSet, basename='ccomments')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include((router.urls, 'article')))
]