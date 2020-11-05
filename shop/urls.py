from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.list_product, name='product_list'),
    path('<slug:product_slug_name>/', views.detail_product, name='product_detail')
]