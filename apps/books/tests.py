# from django.test import TestCase, SimpleTestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.books.models import Book, PublishingHouse, Author


class PublishingHouseTest(APITestCase):
    def test_get_publishing_house(self):
        data={}
        response = self.client.get('http://127.0.0.1:8000/books/api/v1/pub_house/',data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn()

