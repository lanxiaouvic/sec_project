import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

 
class TestBookList(APITestCase):

    @pytest.mark.django_db

    def test_can_get_book_list(self):

        url = reverse('book-list')

        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json()), 0)

class TestBookListAdmin(APITestCase):

    @pytest.mark.django_db

    def test_admin_can_get_book_list(self):

        url = reverse('book-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json()), 0)
