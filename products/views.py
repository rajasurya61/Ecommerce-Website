from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category, Review
from django.shortcuts import render
from .models import Product, ToDoItem
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from .form import ProductForm, CategoryForm

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  # Corrected spelling

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  # Corrected spelling

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  # Corrected spelling


from django.shortcuts import render, redirect
from .models import Product

def productList(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'product_list.html', {'products': products})

def categoryList(request):
    query = request.GET.get('g', '')
    category = Category.objects.filter(name__icontains=query)
    return render(request, 'category_list.html', {'category': category})

def home(request):
    return render(request, "home.html")

def todos(request):
    items = ToDoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})