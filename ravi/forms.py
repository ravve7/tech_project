from django import forms
from ravi.models import Products
from django.forms import ModelChoiceField


class ProductForm(forms.ModelForm):
    selectproduct = forms.ModelChoiceField(
        queryset=Products.objects.all(), label='choose a product', empty_label="select", widget=forms.Select(attrs={"onChange": 'submit()'}))

  
    class Meta:
        model = Products
        fields = ["selectproduct"] 
