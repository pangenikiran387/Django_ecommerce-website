from django import forms
from .models import Category,Product

# category form 
class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

    #validation form
    def clean_category_name(self):
        category_name=self.cleaned_data.get("category_name")

        if Category.objects.filter(category_name=category_name).exists():
            raise forms.ValidationError("category name is already exists")
        return category_name

# product form
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=['product_name','image','category','product_price','description','is_instock']