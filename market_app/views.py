from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem, Order, OrderItem
from .forms import AddProductForm, AddCategoryForm

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

def add_product_view(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddProductForm()
    return render(request, 'add_product.html', {'form': form})


def add_category_view(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddCategoryForm()
    return render(request, 'add_product.html', {'form': form})


def add_to_cart_view(request, id):
    product = Product.objects.get(id=id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('detail', id=id)
    else:
        return redirect('login')
    
def view_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        context = {
            'cart_items': cart_items,
            'total_price': total_price
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('login')