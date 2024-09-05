from django.contrib import admin

# Enregistre modèl ou yo pou yo ka administre atravè entèfas admin Django a

from .models import Product, Order

# Enregistre modèl Product la pou li ka jere nan admin Django a
admin.site.register(Product)

# Enregistre modèl Order la pou li ka jere nan admin Django a
admin.site.register(Order)
