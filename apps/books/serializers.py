from rest_framework import serializers
from apps.books.models import *
from ..signal.post_save import log_book_save, log_author_save, log_publish_house_save
from ..signal.pre_delete import save_delete_log


class PublishingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
