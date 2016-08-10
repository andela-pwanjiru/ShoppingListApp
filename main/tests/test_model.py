from django.test import TestCase
from django.contrib.auth.models import User
from main.models import ShoppingList, ShoppingListItem


class ShoppingListModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='userone',
            password='password')
        self.shoppinglist = ShoppingList.objects.create(
            title='shoppinglistone', user=self.user)
        self.listitem = ShoppingListItem.objects.create(
            listitem='item_one', shoppinglist=self.shoppinglist)

    def tearDown(self):
        User.objects.all().delete()
        ShoppingList.objects.all().delete()
        ShoppingListItem.objects.all().delete()

    def test_user_registration(self):
        """Test that a user is able to register"""
        self.assertEqual(self.user.get_username(), 'userone')
        self.assertIsInstance(self.user, User)

    def test_shoppinglist_creation(self):
        """Test that a user can create a shoppinglist"""
        self.assertTrue(ShoppingList.objects.all())
        self.assertIn('shoppinglistone',
                      ShoppingList.objects.get(title='shoppinglistone').title)
        self.assertIsInstance(self.shoppinglist, ShoppingList)

    def test_shoppinglistitem_creation(self):
        """Test that a user can create a shoppinglist item"""
        self.assertTrue(ShoppingListItem.objects.all())
        self.assertIn('item_one',
                      ShoppingListItem.objects.get(listitem='item_one').listitem)
        self.assertIsInstance(self.listitem, ShoppingListItem)        