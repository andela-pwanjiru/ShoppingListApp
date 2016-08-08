from django import forms
from .models import User, ShoppingList, ShoppingListItem
from django.contrib.auth.models import User


class ShoppingListForm(forms.ModelForm):
    """Form for creation of a shopping list"""
    title = forms.CharField()

    class Meta:
        model = ShoppingList
        fields = ['title']


class ShoppingListItemForm(forms.ModelForm):
    """Form for creation of a shopping list item."""

    class Meta:
        model = ShoppingListItem
        fields = ['listitem', 'shoppinglist']
