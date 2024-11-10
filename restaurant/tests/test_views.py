from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import Menu

class MenuViewTest(APITestCase):
    def setUp(self):
        # Create a user and obtain a token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)

        # Create test menu items
        Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        Menu.objects.create(title="Burger", price=8.99, inventory=30)

    def test_get_all_items(self):
        # Use the correct URL name for the menu items list
        url = reverse('menu-items')
        
        # Use the token for authentication
        response = self.client.get(url, HTTP_AUTHORIZATION='Token ' + self.token.key)
        items = Menu.objects.all()
        
        # Check if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the serialized data matches the expected data
        self.assertEqual(len(response.data), items.count())