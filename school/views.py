from django.shortcuts import render
from django.http import HttpResponse

from .models import Standard, Category
# Create your views here.
def index(request):
    return render(request, 'index.html')

def standards(request):
    standard = Standard.objects.all().values_list('class_name',flat=True)
    context = {
        'standard': standard
    }
    return render(request, 'standards.html', context)

def categories(request):
    category = Category.objects.all().values_list('category_name', flat=True)
    context = {
        'category': category
    }
    return render(request, 'categories.html', context)
