from django.shortcuts import render
from .models import Category, Notebook
# Create your views here.

def category(request):
    category_list = Category.objects.all()
    return render(request, 'category.html', context={
        'category_list':category_list
    })

def notebook(request, id):
    category_filter = Category.objects.filter(pk=id)
    return render(request, 'notebook.html', context={
        'category_filter':category_filter
    })