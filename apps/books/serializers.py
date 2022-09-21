from rest_framework import serializers
from apps.books.models import Author, PublishingHouse, Book
# from apps.signal.post_save import publish_house_save_log, author_save_log, book_save_log
# from apps.signal.pre_delete import delete_book_log, delete_author_log, delete_publishing_house_log
# from apps.signal.update import book_post_init_log, book_post_save_log, \
#     publish_house_post_init_log, publish_house_post_save_log, author_post_init_log, author_post_save_log
# from apps.books.task import inform_new


# class PublishingHouseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PublishingHouse
#         fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
