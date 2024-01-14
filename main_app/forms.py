# forms.py

from django import forms

class RealtySearchForm(forms.Form):
    reference_number = forms.CharField(label='Reference Number', required=True)
    culture_id = forms.CharField(label='Culture ID', required=True)
