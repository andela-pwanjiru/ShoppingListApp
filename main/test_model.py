from django.test import TestCase


class ShoppingListModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='userone',
            password='password')
        self.shoppinglist = ShoppingList.objects.create(
            name='shoppinglistone', user=self.user)
        self.listitem = ShoppingListItem.objects.create(
            name='item_one', shoppinglist=self.shoppinglist)

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
                      ShoppingList.objects.get(name='shoppinglistone').name)
        self.assertIsInstance(self.shoppinglist, ShoppingList)

    def test_shoppinglistitem_creation(self):
        """Test that a user can create a shoppinglist item"""
        self.assertTrue(ShoppingListItem.objects.all())
        self.assertIn('item_one',
                      ShoppingListItem.objects.get(name='item_one').name)
        self.assertIsInstance(self.listitem, ShoppingListItem)        