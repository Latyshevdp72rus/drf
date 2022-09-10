from django.db.models.signals import pre_delete
from django.dispatch import receiver
from apps.books.models import Book, Author
import logging


@receiver(pre_delete, sender=Book)
def delete_book_log(sender, instance, **kwargs):
    logging.warning(f"Произошло удаление книги:{sender} Название книги {instance.book_name} ")


@receiver(pre_delete, sender=Author)
def delete_author_log(sender, instance, **kwargs):
    logging.warning(f"Произошло удаление книги:{sender} Название книги  {instance.first_name} {instance.last_name} {instance.fathername}  ")
