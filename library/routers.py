from rest_framework import routers
from book.viewsets import BookViewSet, AuthorViewSet, CategoryViewSet

router = routers.DefaultRouter()

router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'category', CategoryViewSet)
