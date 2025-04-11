from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_str(self):
        item = Menu.objects.create(title="Pizza", price=120.0, inventory=10)
        expected_str = "Pizza : 120.0"
        self.assertEqual(str(item), expected_str)