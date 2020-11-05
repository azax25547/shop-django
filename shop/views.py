from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddForm

# Create your views here.
def list_product(request):
    products = Product.objects.all()
    category = Category.objects.all()
    cart_product_form = CartAddForm()
    return render(request,'shop/product/detail.html' ,{'products':products ,'cat':category, 'cart_form':cart_product_form})

def detail_product(request, product_slug_name):
    product = get_object_or_404(Product, slug=product_slug_name)
    return render(request, 'shop/product/list.html',{'product':product, 'numbers':range(1,11)})