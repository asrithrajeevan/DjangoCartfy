from django import forms
from .models import Product
from django.core.validators import FileExtensionValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email", "first_name", "last_name", "password1","password2" )




class ProductForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product name', 'style': 'width: 200px;'}))
    product_price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Product price', 'style': 'width: 200px;'}))
    product_image = forms.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        widget=forms.FileInput(attrs={'accept': 'image/*', 'style': 'width: 250px;'})
    )
    product_category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Product Category', 'style': 'width: 200px;'}))

    class Meta:
        model = Product
        fields = "__all__"
        
        labels = {
            "product_name": "Product name: ",
            "product_price": "Price: ",
            "product_image": " Upload image",
            "product_category" : "Category"
        }



class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "product_name": forms.TextInput(attrs={"style": 'width: 300px;'}),
            "product_price": forms.NumberInput(attrs={"style": 'width: 300px;'}),
            "product_category" : forms.TextInput(attrs={"style": 'width: 300px;'}),
            }
        

class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_price', 'product_category']
        widgets = {
            "product_name": forms.TextInput(attrs={"style": 'width: 300px;'}),
            "product_price": forms.NumberInput(attrs={"style": 'width: 300px;'}),
            "product_category" : forms.TextInput(attrs={"style": 'width: 300px;'}),
            }
