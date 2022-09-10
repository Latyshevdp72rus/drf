from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.books.models import Book, Author, PublishingHouse
import logging

# КНИГИ
@receiver(post_save, sender=Book)
def book_save_log(sender, instance, created, **kwargs):
    if created:
        logging.warning(f"В таблице Book, появилась новая запись  {instance.book_name}")

# Публикация
@receiver(post_save, sender=PublishingHouse)
def publish_house_save_log(sender, instance, created, **kwargs):
    if created:
        logging.warning(f"В таблице PublishingHouse, появилась новая запись  {instance.publishing_house_name} ")

# Авторы
@receiver(post_save, sender=Author)
def author_save_log(sender, instance, created, **kwargs):
    if created:
        logging.warning(
            f"В таблице Author, появилась новая запись {instance.first_name} {instance.last_name} {instance.fathername}")


