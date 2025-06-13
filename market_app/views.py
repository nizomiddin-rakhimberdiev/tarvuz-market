from django.shortcuts import render
from .models import Product

# Create your views here.
def home_page(request):
    products = Product.objects.all()
    query = request.POST.get('search')
    print(query)
    if query:
        products = Product.objects.filter(name__icontains=query)
    context = {
        'products': products
    }

    return render(request, 'index.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context)