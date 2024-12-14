from django import forms
from .models import IceCream


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price', 'available']
        labels = {
            'name': 'Название',
            'flavor': 'Вкус',
            'price': 'Цена',
            'available': 'В наличии',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'flavor': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
