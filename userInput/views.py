from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
import requests


@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'userInput/products.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'userInput/product-form.html', {'form': form})


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'userInput/product-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'userInput/prod-delete-confirm.html', {'product': product})

def home(request):
    return render (request, 'userInput/home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('project-home')
    else:
        form = SignUpForm()
    return render(request, 'userInput/register.html', {'form': form})

def api(request):
    response = requests.get('http://api.ipstack.com/89.106.38.28?access_key=""')
    geodata = response.json()
    return render(request, 'userInput/api.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': ""
    })