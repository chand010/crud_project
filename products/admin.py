from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'price', 'description', 'created_at')
    # Optional: Add search functionality
    search_fields = ('name', 'description')

# Register the model with the custom admin class
admin.site.register(Product, ProductAdmin)