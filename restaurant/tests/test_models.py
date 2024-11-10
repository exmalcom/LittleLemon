from django.test import TestCase
from restaurant.models import MenuItem  # Import the MenuItem model

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a new instance of the MenuItem model
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)

        # Test if the string representation matches the expected format
        self.assertEqual(str(item), "IceCream : 80")
