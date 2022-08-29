from rest_framework.response import Response

from apps.books.models import PublishingHouse
from apps.books.serialzers import PublishingHouseSerializer
from django.shortcuts import get_object_or_404

from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet


class PublishHouseAction(ViewSet):
    def list(self, request):
        queryset = PublishingHouse.objects.all()
        serializer = PublishingHouseSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk):
        queryset = PublishingHouse.objects.all()
        handler = get_object_or_404(queryset, pk=pk)
        serializer = PublishingHouseSerializer(handler, many=True)
        return Response(serializer.data)

# class PublishingHouseAction(CreateAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer
#
#
# class PubViewDetail(RetrieveUpdateDestroyAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer
#
#
# class PublishingHouseAction(CreateModelMixin, ListAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer


# from rest_framework import status


# from rest_framework.views import APIView
# from rest_framework.response import Response
# ,Author,Book
# ,AuthorSerializer,BookSerializer


#     def get_queryset(self):
#         pass
# 1 Способ
# queryset = PublishingHouse.objects.exclude(pk=1)
# return PublishingHouse.objects.exclude(pk=1)
# 2 способ
# filter_value = self.request.get('value')
# return PublishingHouse.objects.exclude(pk=1)


# class PublishingHouseAPIView(APIView):
#     def get(self, request, pk):
#         queryset = PublishingHouse.objects.filter(pk=pk)
#         serializer = PublishingHouseSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         publishing_house =PublishingHouse.objects.get(pk=pk)
#         serializer = PublishingHouseSerializer(instance=publishing_house,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         publishing_house = PublishingHouse.objects.get(pk=pk)
#         publishing_house.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# class PublishingHoueseCreateAPIView(APIView):
#     # разрешаем запросы
#     def post(self, request):
#         serializer = PublishingHouseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# """"""
# class AuthorAPIView(APIView):
#     def get(self, request, pk):
#         queryset = Author.objects.filter(pk=pk)
#         serializer = AuthorSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         author = Author.objects.get(pk=pk)
#         serializer = AuthorSerializer(instance=author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         author = Author.objects.get(pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class AuthorCreateAPIView(APIView):
#     # разрешаем запросы
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookAPIView(APIView):
#     def get(self, request, pk):
#         queryset = Book.objects.filter(pk=pk)
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(instance=book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class BookCreateAPIView(APIView):
#     # разрешаем запросы
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
