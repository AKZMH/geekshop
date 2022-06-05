from django.shortcuts import render

# Create your views here.
from mainapp.models import Product , Category


def index(request):
    context = {
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # links_menu = [
    #     {'href': 'products_all', 'title': 'все'},
    #     {'href': 'products_home', 'title': 'дом'},
    #     {'href': 'products_office', 'title': 'офис'},
    #     {'href': 'products_modern', 'title': 'модерн'},
    #     {'href': 'products_classic', 'title': 'классика'},
    # ]

    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def products_list(request, pk):
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')
