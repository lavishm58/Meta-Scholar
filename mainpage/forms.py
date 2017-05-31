from django.contrib.auth.models import User
from django import forms


class My_User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        field=['username','email','password']