from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.books.models import Book, Author, PublishingHouse


@receiver(post_save, sender=Book)
def log_book_save(sender, instance, created, **kwargs):
    if created:
        print(f"В таблице Book, появилась новая запись {instance.book_name} и она успешно создана")


@receiver(post_save, sender=Author)
def log_author_save(sender, instance, created, **kwargs):
    if created:
        print(f"В таблице Author, появилась новая запись {instance.first_name} {instance.last_name} \
                {instance.fathername} и она успешно создана")


@receiver(post_save, sender=PublishingHouse)
def log_publish_house_save(sender, instance, created, **kwargs):
    if created:
        print(f"В таблице PublishingHouse, появилась новая запись  {instance.publishing_house_name} \
            и она успешно создана")
