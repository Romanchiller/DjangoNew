from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort is None:
        phones = Phone.objects.all()
    if sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    if sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')

    template = 'catalog.html'
    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}

    return render(request, template, context)
