from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from django.conf import settings
import moncashify
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .models import Product, Order

# Kreye vizyon ou yo isit la.

def store(request):
    # Ranmase tout pwodwi ki egziste yo nan bazdone a
    products = Product.objects.all()

    # Kreye yon konteks ak pwodwi yo pou pase nan modèl la
    context = {'products': products}

    # Rende paj 'store.html' ak konteks la
    return render(request, 'base/store.html', context)

def checkout(request, pk):
    # Jwenn pwodwi ki gen ID a ki koresponn ak 'pk' la
    product = Product.objects.get(id=pk)

    # Kreye yon konteks ak pwodwi a pou pase nan modèl la
    context = {'product': product}

    # Rende paj 'checkout.html' ak konteks la
    return render(request, 'base/checkout.html', context)

def paymentComplete(request):
    # Chaje kò demann lan kòm JSON
    body = json.loads(request.body)

    # Affiche kò a nan konsole a pou debogaj
    print('BODY:', body)

    # Retounen yon repons JSON ki di 'Payment completed!'
    return JsonResponse('Payment completed!', safe=False)

@login_required
def moncash(request, product_id):
    # Asire w ke itilizatè a otantifye
    if not request.user.is_authenticated:
        # Jwenn URL pou konekte itilizatè a
        login_url = reverse('accounts:login_user')

        # Redireksyon itilizatè a sou paj koneksyon an ak URL aktyèl la
        return redirect(f'{login_url}?next={request.get_full_path()}')

    # Jwenn pwodwi itilizatè a vle achte a, oswa montre yon 404 si li pa jwenn
    product = get_object_or_404(Product, id=product_id)

    # Kreye yon nouvo lòd ak pwodwi sa a
    order = Order.objects.create(product=product)

    # Pri pwodwi a pral itilize kòm montan total la
    total_amount = product.price

    # Kreye yon ID inik pou lòd la
    order_id = f'Order_{order.id}_{request.user.id}'

    # Konfigire API MonCash la
    moncash = moncashify.API(settings.MONCASH['CLIENT_ID'], settings.MONCASH['SECRET_KEY'], True)

    # Kreye yon nouvo peman ak MonCash
    payment = moncash.payment(order_id, total_amount)

    # Redireksyon itilizatè a nan paj peman MonCash la
    return redirect(payment.redirect_url)
