from django.db.models.signals import pre_delete
from django.dispatch import receiver
from apps.books.models import Book, Author, PublishingHouse
import logging

logging.basicConfig(filename='apps/signal/delete.log',
                    level=logging.warning, encoding='cp1251')


# КНИГИ
@receiver(pre_delete, sender=Book)
def delete_book_log(sender, instance, **kwargs):
    logging.warning(f'Table the "Book", entry has been deleted: "{instance.book_name}" ')


# издательства
@receiver(pre_delete, sender=PublishingHouse)
def delete_publishing_house_log(sender, instance,  **kwargs):
    logging.warning(f'Table the "PublishingHouse",entry has been deleted: "{instance.publishing_house_name}"')


# Авторыы
@receiver(pre_delete, sender=Author)
def delete_author_log(sender, instance,  **kwargs):
    logging.warning(
            f'Table the "Author", entry has been deleted: "{instance.first_name} {instance.last_name} {instance.fathername}"')
