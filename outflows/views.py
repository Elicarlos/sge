from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Outflow
from .forms import OutflowModelForm


class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        
        if product:
            queryset = queryset.filter(product__title__icontains=product)
            
        return queryset
    
    
class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class =  OutflowModelForm
    success_url = reverse_lazy('outflow_list')
    
class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'

