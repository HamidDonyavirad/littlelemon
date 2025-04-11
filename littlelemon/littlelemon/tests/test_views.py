from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Pizza", price=100, inventory=10)
        self.item2 = Menu.objects.create(title="Burger", price=80, inventory=20)
        self.item3 = Menu.objects.create(title="Pasta", price=90, inventory=15)
        self.client = APIClient()
    def test_getall(self):
        response = self.client.get('/restaurant/menu/') 
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)   