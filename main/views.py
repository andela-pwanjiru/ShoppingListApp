from django.shortcuts import render

from .models import ShoppingList, ShoppingListItem

# Create your views here.
class LoginView(TemplateView):
    """Handles login of users"""
    def get(self, request):
        return render(request, 'login.html')
