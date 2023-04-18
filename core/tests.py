from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Bet
from .serializers import UserListSerializer


class UserViewTests(APITestCase):
    def test_create_user(self):
        client = APIClient()
        url = reverse('user-create')
        data = {'id': 'test_id', 'email': 'test@example.com'}
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], data['id'])
        self.assertEqual(response.data['email'], data['email'])

    def test_list_users(self):
        user1 = User.objects.create(id='test_id1', email='test1@example.com')
        user2 = User.objects.create(id='test_id2', email='test2@example.com')

        client = APIClient()
        url = reverse('user-list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        serializer = UserListSerializer([user1, user2], many=True)
        self.assertEqual(response.data, serializer.data)


class BetCreateViewTestCase(APITestCase):
    def test_create_bet(self):
        url = reverse('bet-create')
        user = User.objects.create(id='test_id1', email='test1@example.com')
        data = {
            'user': user.id,
            'game1': 'test1',
            'game2': 'test2',
            'game3': 'test3',
            'game4': 'test4',
            'game5': 'test5',
            'game6': 'test6',
            'game7': 'test7',
            'game8': 'test8',
            'game9': 'test9'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, data)
        self.assertEqual(data['user'], data['user'])
        self.assertEqual(data['game1'], data['game1'])
        self.assertEqual(data['game2'], data['game2'])
        self.assertEqual(data['game3'], data['game3'])
        self.assertEqual(data['game4'], data['game4'])
        self.assertEqual(data['game5'], data['game5'])
        self.assertEqual(data['game6'], data['game6'])
        self.assertEqual(data['game7'], data['game7'])
        self.assertEqual(data['game8'], data['game8'])
        self.assertEqual(data['game9'], data['game9'])
