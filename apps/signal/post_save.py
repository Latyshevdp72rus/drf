from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.books.models import Book, Author, PublishingHouse


@receiver(post_save, sender=Book)
def log_book_save(sender, instance, created, **kwargs):
    if created:
        print(f"Book {instance.book_name} is created")


@receiver(post_save, sender=Author)
def log_book_save(sender, instance, created, **kwargs):
    if created:
        print(f"Author {instance.first_name}{instance.last_name}{instance.fathername} is created")


@receiver(post_save, sender=PublishingHouse)
def log_book_save(sender, instance, created, **kwargs):
    if created:
        print(f"PublishingHouse {instance.publishing_house_name} is created")
