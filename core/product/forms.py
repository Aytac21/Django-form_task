from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    tax_price = forms.FloatField(label='Tax Price')

    class Meta:
        model = Product
        fields = ['name', 'price', 'discount_price', 'tax_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'tax_price': forms.NumberInput(attrs = {'class': 'form-control'})
        }
    

    def clean(self):
        price = self.cleaned_data.get('price')
        discount_price = self.cleaned_data.get('discount_price', 0)
        tax_price = self.cleaned_data.get('tax_price', 0)
    
        if(price-discount_price+tax_price == 0):
            raise forms.ValidationError("price tax_price ile discount_price-in ferqinden boyuk olmalidir")

        return super().clean()
    
    def save(self, commit=True):
        self.cleaned_data["name"] = self.cleaned_data["name"].upper()
        del self.cleaned_data["tax_price"]
        
        if commit:
            product = Product.objects.create(**self.cleaned_data)
        else:
            product = Product(**self.cleaned_data)
        
        return product
