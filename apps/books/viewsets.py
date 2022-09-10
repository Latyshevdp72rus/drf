from apps.books.serializers import AuthorSerializer,BookSerializer,PublishingHouseSerializer
from apps.books.models import Author, PublishingHouse, Book
from rest_framework import viewsets


class PublishingHouseViewSet(viewsets.ModelViewSet):
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingHouseSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
