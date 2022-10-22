from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.books.models import PublishingHouse,Author,Book
from apps.books.serialzers import PublishingHouseSerializer,AuthorSerializer,BookSerializer


class PublishingHouseAPIView(APIView):
    def get(self, request, pk):
        queryset = PublishingHouse.objects.filter(pk=pk)
        serializer = PublishingHouseSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        publishing_house =PublishingHouse.objects.get(pk=pk)
        serializer = PublishingHouseSerializer(instance=publishing_house,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        publishing_house = PublishingHouse.objects.get(pk=pk)
        publishing_house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PublishingHoueseCreateAPIView(APIView):
    # разрешаем запросы
    def post(self, request):
        serializer = PublishingHouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""""""
class AuthorAPIView(APIView):
    def get(self, request, pk):
        queryset = Author.objects.filter(pk=pk)
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorCreateAPIView(APIView):
    # разрешаем запросы
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPIView(APIView):
    def get(self, request, pk):
        queryset = Book.objects.filter(pk=pk)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookCreateAPIView(APIView):
    # разрешаем запросы
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
