from django.test import TestCase, Client
from django.contrib.auth.models import User
# Bookモデルを取ってこよう
from shop.models import Book
from unittest.mock import ANY

class TestHoge(TestCase):
    # ここでfixtures読む
    fixtures = ['hoge.json']

    def test_1(self):
        client = Client()
        # cookie認証の時のみ
        client.force_login(User.objects.get(pk=1))
        response = client.post(
            '/api/v1/books/',
            data={
                'title': 'DRFの教科書',
                'price': 500,
            }
        )
        self.assertEqual(
            {'id': ANY, 'title': 'DRFの教科書', 'price': 500},
            response.json()
        )
        # assert書く
        self.assertEqual(True, Book.objects.filter(title='DRFの教科書', price=500).exists())
        
    def test_2(self):
        client = Client()
        # cookie認証の時のみ
        client.force_login(User.objects.get(pk=1))
        response = client.put(
            '/api/v1/books/eb126e87-1a5f-4e36-974f-c5ffa4c9424f/',
            data={
                'title': 'naiyatu',
                'price': 500,
            },
            content_type='application/json',
        )
        # print(response.status_code)
        # print(response.json())
        self.assertEqual(True, Book.objects.filter(pk="eb126e87-1a5f-4e36-974f-c5ffa4c9424f", title='naiyatu', price=500).exists())
