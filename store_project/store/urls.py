from django.urls import path
from .views import product_list, category_list, product_detail, category_detail, save_order

urlpatterns = [
    path('', product_list, name='store'),
    path('cats/', category_list, name='cats'),
    path('product/<int:pk>/', product_detail, name='product'),
    path('category/<int:pk>/', category_detail, name='category'),
    path('save_order', save_order, name='product'),
]