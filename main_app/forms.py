# forms.py

from django import forms

class RealtySearchForm(forms.Form):
    min_list_price = forms.DecimalField(label='Minimum List Price', required=False, max_digits=15, decimal_places=2)
    max_list_price = forms.DecimalField(label='Maximum List Price', required=False, max_digits=15, decimal_places=2)
    bedrooms = forms.IntegerField(label='Number of Bedrooms', required=False, min_value=0, max_value=99)
    bathrooms = forms.IntegerField(label='Number of Bathrooms', required=False, min_value=0, max_value=99)
