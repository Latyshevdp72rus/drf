# from django.test import TestCase, SimpleTestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.books.models import Book, PublishingHouse, Author


class BookTest(APITestCase):
    def get_book(self):


