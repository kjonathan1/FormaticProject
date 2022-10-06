from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json



class DateInput(forms.DateInput):
    input_type = 'date'


class UserLoginForm(forms.ModelForm):
   
    username = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
        required=True)

    class Meta:
        model = User
        fields = ['username','password']




class ProductForm(forms.ModelForm):
    class meta:
        model = Product
        fields = ['title', 'description']


class ClientForm(ModelForm):
    class meta:
        # model = Client
        fields = ['clientName', 'province']

class ClientForm2(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"



class InvoiceForm(forms.ModelForm):
    class meta:
        model = Invoice
        fields = ['title', 'notes', 'dueDate']


class SettingsForm(forms.ModelForm):
    class meta:
        model = Settings
        fields = ['clientName', 'clientLogo', 'province']

