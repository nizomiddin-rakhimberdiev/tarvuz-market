from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem, Order, OrderItem, Comment
from .forms import AddProductForm, AddCategoryForm, EditProfileForm
from users.models import CustomUser
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = request.POST.get('comment')
            Comment.objects.create(text=comment, product=product, user=request.user)
            return redirect('detail', id=id)
        else:
            return redirect('login')
    comments = Comment.objects.filter(product=product)
    context = {
        'product': product,
        'comments': comments
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
    return render(request, 'detail.html', {'product': product})

@login_required(login_url='login')
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
    
@login_required(login_url='login')
def remove_from_cart(request, id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=id, cart=cart)
        if cart_item:
            cart_item.delete()
            return redirect('view_cart')
    else:
        return redirect('login')
    return render(request, 'cart.html')

@login_required(login_url='login')
def profile_view(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            form.save()
            user.username = phone_number
            user.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user)
    context = {
        'user': user,
        'form': form
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def plus_cart_view(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required(login_url='login')
def minus_cart_view(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect('view_cart')


@login_required(login_url='login')
def order_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        address = request.POST.get('address')
        order = Order.objects.create(user=request.user, total_price=total_price, address=address)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart_items.delete()
        return redirect('home')
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'order.html', context)

@login_required(login_url='login')
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    context = {
        'orders': orders
    }
    return render(request, 'order_history.html', context)