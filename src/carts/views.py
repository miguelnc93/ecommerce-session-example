from django.shortcuts import render, redirect
from .models import Cart
from products.models import *

# Create your views here.

def cart_create(user):
    user_obj = None
    if user is not None:
        if user.is_authenticated():
            user_obj = user
    cart_obj = Cart.objects.create(user=user_obj)
    print("create new cart")
    return cart_obj

def cart_new_or_get(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        new_object = False #flag to know if a session already exists
        print("ya existe cart id")
        cart_obj = qs.first()
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = cart_create(request.user)
        new_object = True
        #print(request.user)
        request.session['cart_id'] = cart_obj.id
    return cart_obj,new_object

def cart_home(request):
    cart_obj, new_obj = cart_new_or_get(request)
    return render(request,"carts/home.html", {})

def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = cart_new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    return redirect("cart:home")
