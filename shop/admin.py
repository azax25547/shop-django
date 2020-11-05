from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','updated_at')