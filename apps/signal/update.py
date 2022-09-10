from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from apps.books.models import Book, PublishingHouse, Author
import logging

logging.basicConfig(filename='apps/signal/update.log', level=logging.warning, encoding='cp1251')

# КНИГИ
@receiver(post_init, sender=Book)
def book_post_init_log(instance, **kwargs):
    instance.original_name = instance.book_name


@receiver(post_save, sender=Book)
def book_post_save_log(instance, **kwargs):
    if not instance.book_name == instance.original_name:
        logging.warning(f'Запись  "{instance.original_name}" было изменено! на "{instance.book_name}"')


# издательства
@receiver(post_init, sender=PublishingHouse)
def publish_house_post_init_log(instance, **kwargs):
    instance.original_name = instance.publishing_house_name


@receiver(post_save, sender=PublishingHouse)
def publish_house_post_save_log(instance, **kwargs):
    if not instance.publishing_house_name == instance.original_name:
        logging.warning(f'Запись "{instance.original_name}" было изменено! на "{instance.publishing_house_name}"')


# Авторы
@receiver(post_init, sender=Author)
def author_post_init_log(instance, **kwargs):
    instance.original_name = instance.first_name + instance.last_name


@receiver(post_save, sender=Author)
def author_post_save_log(instance, **kwargs):
    if not instance.first_name + instance.last_name == instance.original_name:
        logging.warning(
            f'Запись "{instance.original_name}" было изменено! на "{instance.first_name} {instance.last_name}"')
