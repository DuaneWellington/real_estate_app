# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from .models import User, Folder

class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email')
        # Add UniqueValidator for username and email
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        validators = {
            'email': [EmailValidator(message='This email is already taken.')],
        }
        
class RealtySearchForm(forms.Form):
    min_list_price = forms.DecimalField(label='Minimum List Price', required=False, max_digits=15, decimal_places=2)
    max_list_price = forms.DecimalField(label='Maximum List Price', required=False, max_digits=15, decimal_places=2)
    bedrooms = forms.IntegerField(label='Number of Bedrooms', required=False, min_value=0, max_value=99)
    bathrooms = forms.IntegerField(label='Number of Bathrooms', required=False, min_value=0, max_value=99)

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FolderCreateForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FolderUpdateForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class SaveListingForm(forms.Form):
    listing_id = forms.CharField(label='Listing ID', max_length=100)