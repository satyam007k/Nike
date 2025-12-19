from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
from .models import Category, Product, Cart, CartItem, Order, OrderItem

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'nikeapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'nikeapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)[:8]  # Featured products
    return render(request, 'nikeapp/home.html', {'categories': categories, 'products': products})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'nikeapp/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    related_products = product.category.products.filter(available=True).exclude(id=product.id)[:4]
    return render(request, 'nikeapp/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total = sum(item.get_total for item in cart.items.all())
    return render(request, 'nikeapp/cart.html', {'cart': cart, 'total': total})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')

@login_required
def cart_remove_all(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        return redirect('cart_detail')
    
    # Create order and mark as paid (no payment gateway)
    order = Order.objects.create(user=request.user, paid=True)
    for item in cart.items.all():
        OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
    
    # Clear cart
    cart.items.all().delete()
    
    return redirect('checkout_success')

@login_required
def checkout_success(request):
    # Get the latest order for the user
    order = Order.objects.filter(user=request.user).latest('created')
    return render(request, 'nikeapp/checkout_success.html', {'order': order})
