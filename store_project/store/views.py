from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Order

# Create your views here.
def build_table(lst, cols):
    return [lst[i:i+cols] for i in range(0, len(lst), cols)]

def save_order(request):
    product=Product.objects.get(pk=request.POST["product_id"])
    order=Order()
    order.name=request.POST["username"]
    order.email=request.POST["user_e-mail"]
    order.product=product
    order.save()
    return render(request,'store/order.html')

    
def product_list(request):
    search_querry=request.GET.get('search', '')
    if search_querry:
        products=Product.objects.filter(title__icontains=search_querry)
    else:
        products=Product.objects.all()
    return render(request,'store/product_list.html',context={'product_list': build_table(products, 3)})

def category_list(request):
    categories=Category.objects.all()
    return render(request,'store/cats.html',context={'categories': categories})

def product_detail(request, pk):
    product=Product.objects.get(pk=pk)
    return render(request,'store/product_detail.html',context={'product': product})

def category_detail(request, pk):
    category=Category.objects.get(pk=pk)
    products=category.products.all()
    return render(request,'store/category_detail.html',context={'product_list': build_table(products, 3), 'category': category})