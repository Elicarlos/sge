from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product
from .forms import ProductModelForm
from categories.models import Category
from brands.models import Brand


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        serie_number = self.request.GET.get('serie_number')
        
        if title:
            queryset = queryset.filter(title__icontains=title)
            
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
            
        if category:
            queryset = queryset.filter(category__id=category)
            
        if brand:
            queryset = queryset.filter(brand__id=brand)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context
    
    
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class =  ProductModelForm
    success_url = reverse_lazy('product_list')
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductModelForm
    success_url =  reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
