from django.db import models

# Kreye modèl ou yo isit la.

class Product(models.Model):
    # Non pwodwi a
    name = models.CharField(max_length=200)

    # Deskripsyon pwodwi a; ka vid (blank) e ka null (pa gen vale)
    description = models.TextField(null=True, blank=True)

    # URL imaj pwodwi a; ka vid (blank) e ka null (pa gen vale)
    image_url = models.CharField(max_length=1000, null=True, blank=True)

    # Pri pwodwi a; ka vid (blank) e ka null (pa gen vale)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        # Retounen non pwodwi a kòm reprezantan pou modèl sa a
        return self.name


class Order(models.Model):
    # Referans a pwodwi a nan modèl Product; ka vid (blank) e ka null (pa gen vale)
    product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)

    # Dat lè lòd la te kreye; otomatikman ajoute lè lòd la kreye
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Retounen non pwodwi a pou reprezante lòd la
        return self.product.name
