# from rest_framework import routers
# from apps.books.viewsets import PublishingHouseViewSet, BookViewSet, AuthorViewSet
#
#
# router = routers.DefaultRouter()
# router.register(r'pub_house', PublishingHouseViewSet)
# router.register(r'books', BookViewSet)
# router.register(r'authors', AuthorViewSet)
from rest_framework import routers
from apps.books.viewsets import PublishingHouseViewSet, BookViewSet, AuthorViewSet


router = routers.DefaultRouter()
router.register(r'pub_house', PublishingHouseViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
