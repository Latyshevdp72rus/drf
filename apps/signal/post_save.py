from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.books.models import Book, Author, PublishingHouse
import logging

logging.basicConfig(filename='apps/signal/save.log', level=logging.warning, encoding='cp1251')


# КНИГИ
@receiver(post_save, sender=Book)
def book_save_log(sender, instance, created, **kwargs):
    if created:
        logging.warning(f'Table the "Book", new entry created: {instance.book_name}')


# издательства
@receiver(post_save, sender=PublishingHouse)
def publish_house_save_log(sender, instance, created, **kwargs):
    if created:
        logging.warning(f'Table the "PublishingHouse", new entry created:   {instance.publishing_house_name} ')


# Авторы
@receiver(post_save, sender=Author)
def author_save_log(sender, instance, created, **kwargs):
    if created:
        logging.warning(
            f'Table the "Author", new entry created: {instance.first_name} {instance.last_name} {instance.fathername}')
