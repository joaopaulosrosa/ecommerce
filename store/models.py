from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=30, null=False)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    costumer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.id


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=12, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
