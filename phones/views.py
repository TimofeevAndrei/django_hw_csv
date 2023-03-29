from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    list_phone = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': list_phone,
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
