from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up some MenuItems to test
        self.item1 = MenuItem.objects.create(title="Pizza", price=12.99, inventory=50)
        self.item2 = MenuItem.objects.create(title="Burger", price=8.99, inventory=30)
        
        self.client = APIClient()  # Using the DRF APIClient to send requests

    def test_getall(self):
        # Send a GET request to retrieve the menu items
        response = self.client.get('/restaurant/menu/')
        
        # Serialize the data manually
        expected_data = MenuItemSerializer([self.item1, self.item2], many=True).data
        
        # Assert if the response data matches the serialized data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
