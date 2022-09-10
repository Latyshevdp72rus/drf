from django.db.models.signals import pre_delete
from django.dispatch import receiver
from apps.books.models import Book


@receiver(pre_delete, sender=Book)
def save_delete_log(sender, instance, deleted, **kwargs):
    if deleted:
        print(f"Произошло создание новой:{instance} Название книги {sender._meta.get.all_field_names()}")

