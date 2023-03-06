from django.shortcuts import render, get_object_or_404, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        my_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        my_objects = Phone.objects.order_by('-price')
    elif sort == 'max_price':
        my_objects = Phone.objects.all().order_by('price')
    else:
        my_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'my_objects': my_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
