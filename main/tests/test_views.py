from django.core.urlresolvers import reverse
from django.test import TestCase
from main.models import User, ShoppingList, ShoppingListItem


class ShoppinglistViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='anotheruser',
            password='anotherpassword')
        self.login = self.client.login(
            username='anotheruser', password='anotherpassword')
        self.shoppinglist = ShoppingList.objects.create(
            title='list_one', user=self.user)
        self.shoppinglistitem = ShoppingListItem.objects.create(
            listitem='item_one', shoppinglist=self.shoppinglist)

    def tearDown(self):
        ShoppingList.objects.all().delete()
        ShoppingListItem.objects.all().delete()

    def test_shoppinglist_view(self):
        """Tests creation of a shopping list"""
        resp = self.client.get(reverse('main'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ShoppingList.objects.count(), 1)

    def test_shoppinglistitem_view(self):
        """Tests creation of a shopping list items"""
        resp = self.client.get(reverse('items', kwargs={'pk': self.shoppinglist.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ShoppingListItem.objects.count(), 1)    
