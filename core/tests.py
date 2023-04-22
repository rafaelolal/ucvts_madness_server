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
            'order': 'first place*second place*third place'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, data)
        self.assertEqual(data['user'], data['user'])
        self.assertEqual(data['order'], data['order'])
