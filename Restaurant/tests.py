from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from rest_framework import status

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=3, inventory=3)
        self.assertEqual(item.title + ': ' + str(item.price), "IceCream: 3")
        
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="pie", price=5, inventory=2)
        Menu.objects.create(title="pizza", price=12, inventory=8)
        Menu.objects.create(title="tiramisu", price=6, inventory=2)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_objects = Menu.objects.all()

        serializer = MenuSerializer(menu_objects, many=True)

        self.assertEqual(response.data, serializer.data)