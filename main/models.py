from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ShoppingList(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="user")

    def __unicode__(self):
        return u'%s' % self.title


class ShoppingListItem(models.Model):

    listitem = models.CharField(max_length=255)
    # bought = models.BooleanField()
    shoppinglist = models.ForeignKey(ShoppingList, related_name='items')

    def __unicode__(self):
        return u'%s' % self.listitem
