from django import forms
from . models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price']
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class':'form-control'}), 
            'cost_price': forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3})
        }
        
        labels = {
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Numero de Serie',
            'cost_price': 'Preço de custo',
            'selling_price': 'Preco de Venda'
        }