from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from apps.books.serializers import AuthorSerializer, BookSerializer\
    # , PublishingHouseSerializer
from apps.books.models import Author, PublishingHouse, Book
from rest_framework import viewsets, status
from apps.books.task import inform_new
from rest_framework.views import APIView


class AuthorViewSet(APIView):
    def post(self, request):
        data = request.data
        author = Author(**data)
        author.save()
        inform_new.delay()
        return Response(status=status.HTTP_202_ACCEPTED)



            #
# class PublishingHouseViewSet(viewsets.ModelViewSet):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer()
#
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
