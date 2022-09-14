from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from apps.books.serializers import AuthorSerializer, BookSerializer, PublishingHouseSerializer
from apps.books.models import Author, PublishingHouse, Book
from rest_framework import viewsets
from apps.books.task import inform_new


class PublishingHouseViewSet(viewsets.ModelViewSet):
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingHouseSerializer

    def list(self, request):
        queryset = PublishingHouse.objects.all()
        serializer = PublishingHouseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = PublishingHouse.objects.all()
        handler = get_object_or_404(queryset, pk=pk)
        serializer = PublishingHouseSerializer(handler, many=True)
        return Response(serializer.data)

    def create(self, request):
        inform_new.delay()


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#
# class PublishHouseAction(ViewSet):
#     def list(self, request):
#         queryset = PublishingHouse.objects.all()
#         serializer = PublishingHouseSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         queryset = PublishingHouse.objects.all()
#         handler = get_object_or_404(queryset, pk=pk)
#         serializer = PublishingHouseSerializer(handler, many=True)
#         return Response(serializer.data)
#
#     @inform_new
#     def create(self, request):
#         pass
