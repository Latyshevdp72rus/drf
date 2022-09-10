from django.db.models.signals import pre_delete
from django.dispatch import receiver
from apps.books.models import Book, Author, PublishingHouse
import logging


@receiver(pre_delete, sender=Book)
def delete_book_log(sender, instance, deleted, **kwargs):
    if deleted:
        logging.warning(f"В таблице Book, произошло удаление записи: {instance.book_name} ")


@receiver(pre_delete, sender=PublishingHouse)
def delete_publishing_house_log(sender, instance, deleted, **kwargs):
    if deleted:
        logging.warning(f"В таблице PublishingHouse, произошло удаление записи: {instance.publishing_house_name}")


@receiver(pre_delete, sender=Author)
def delete_author_log(sender, instance, deleted, **kwargs):
    if deleted:
        logging.warning(
            f"В таблице Author, произошло удаление записи: {instance.first_name} {instance.last_name} {instance.fathername}")
