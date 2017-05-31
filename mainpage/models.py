from django.db import models
# import pickle
# import base64

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# from oauth2client.contrib.django_util.storage import DjangoORMStorage
# from oauth2client.contrib.django_util.models import CredentialsField

class social_auth_usersocialauth(models.Model):
    query = models.TextField(max_length=254)

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobilephone = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username

# class CredentialsModel(models.Model):
#     id = models.ForeignKey(User, primary_key=True)
#     credential = CredentialsField()
#
# class CredentialsAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(CredentialsModel, CredentialsAdmin)

