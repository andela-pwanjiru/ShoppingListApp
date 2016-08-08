from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShoppingList, ShoppingListItem
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .forms import ShoppingListForm, ShoppingListItemForm
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
class LoginView(TemplateView):
    """Handles login of users"""
    def get(self, request):
        return render(request, 'login.html')


class ShoppingView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    """View to create and return list of bucketlist"""
    template_name = 'shopping.html'
    success_url = '/main'
    model = ShoppingList
    fields = ['title']

    def form_valid(self, form):
        shoppinglist = form.save(commit=False)
        shoppinglist.user = self.request.user
        return super(ShoppingView, self).form_valid(form)

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user.id)


class ShoppingItemsView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'items.html'
    model = ShoppingListItem
    fields = ['listitem']

    def form_valid(self, form, *args, **kwargs):

        shop_pk = self.kwargs.get('pk')
        self.success_url = '/main/' + shop_pk + '/items/'
        related = ShoppingList.objects.get(pk=shop_pk)
        itemlist = form.save(commit=False)
        itemlist.shoppinglist = related
        return super(ShoppingItemsView, self).form_valid(form)

    def get_queryset(self):
        return ShoppingListItem.objects.all()
