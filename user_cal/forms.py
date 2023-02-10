# import the standard Django Forms
# from built-in library
from django import forms

class UserCalForm(forms.Form):
    height = forms.IntegerField()
    weight = forms.DecimalField(max_digits=5, decimal_places=2)
    age = forms.IntegerField()