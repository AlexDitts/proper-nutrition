from .models.models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ExcludeProductsForm(forms.ModelForm):
    title = forms.MultipleChoiceField(choices=[tuple(i.values()) for i in Product.objects.values('pk', 'title')])

    class Meta:
        model = Product
        fields = ['title']
