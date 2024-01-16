# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
class CustomUserCreationForm(UserCreationForm):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('firstname', 'lastname')
class RealtySearchForm(forms.Form):
    min_list_price = forms.DecimalField(label='Minimum List Price', required=False, max_digits=15, decimal_places=2)
    max_list_price = forms.DecimalField(label='Maximum List Price', required=False, max_digits=15, decimal_places=2)
    bedrooms = forms.IntegerField(label='Number of Bedrooms', required=False, min_value=0, max_value=99)
    bathrooms = forms.IntegerField(label='Number of Bathrooms', required=False, min_value=0, max_value=99)
