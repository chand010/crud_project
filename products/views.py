from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')