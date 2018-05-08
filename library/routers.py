from rest_framework import routers
from book.viewsets import BookViewSet, AuthorViewSet, CategoryViewSet
from account.viewsets import UserViewSet, GroupViewSet


router = routers.DefaultRouter()

router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'category', CategoryViewSet)

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
