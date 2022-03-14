from math import fabs
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cartData, cookieCart, guestOrder

# Create your views here.

def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    products  = Product.objects.all()

    context = {
        'products' : products,
        'cartItems': cartItems
    }
    return render(request, 'store/store.html', context)

def product(request, pk):
    data = cartData(request)

    product   = Product.objects.get(id=pk)
    cartItems = data['cartItems']
    order     = data['order']

    if request.user.is_authenticated:
        item     = OrderItem.objects.get_or_create(order=order, product=product)[0]
        quantity = item.quantity
    else:
        quantity = ''
        try:
            for i in data['items']:
                if i['product'] == product:
                    quantity = i['quantity']
        except:
            pass

    context = {
        'product'  : product,
        'order'    : order,
        'cartItems': cartItems,
        'quantity' : quantity,
    }
    return render(request, 'store/product.html', context)

def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order     = data['order']
    items     = data['items']

    context = {
        'items'    : items,
        'order'    : order,
        'cartItems': cartItems
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order     = data['order']
    items     = data['items']

    context = {
        'items'    : items,
        'order'    : order,
        'cartItems': cartItems
    }
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data      = json.loads(request.body)
    productId = data['productId']
    action    = data['action']

    customer       = request.user.customer
    product        = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    context = {

    }

    return JsonResponse('Item was added!', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data           = json.loads(request.body)

    if request.user.is_authenticated:
        customer       = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total                = float(data['form']['total'])
    order.transaction_id = transaction_id

    if "%.2f" % round(total, 2) == "%.2f" % round(order.get_cart_total, 2):
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer = customer,
        order    = order,
        address  = data['shipping']['address'],
        city     = data['shipping']['city'],
        state    = data['shipping']['state'],
        zip_code = data['shipping']['zipcode'],
    )

    return JsonResponse('Payment complete!', safe=False)
