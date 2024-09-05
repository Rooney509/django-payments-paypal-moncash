from django.urls import path
from . import views

app_name = 'base'  # Defini non aplikasyon an pou itilize nan URL yo

urlpatterns = [
    # URL pou paj magazen an, ki itilize fonksyon 'store' nan 'views.py'
    path('', views.store, name="store"),

    # URL pou paj checkout la ak ID pwodwi a, ki itilize fonksyon 'checkout' nan 'views.py'
    path('checkout/<int:pk>/', views.checkout, name="checkout"),

    # URL pou paj konfimasyon peman an, ki itilize fonksyon 'paymentComplete' nan 'views.py'
    path('complete/', views.paymentComplete, name="complete"),

    # URL pou paj MonCash la ak ID pwodwi a, ki itilize fonksyon 'moncash' nan 'views.py'
    path('moncash/<int:product_id>/', views.moncash, name='moncash'),
]
