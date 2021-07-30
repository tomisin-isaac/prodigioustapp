from django.db import models
from django.contrib.auth.models import User
# from django.forms import NumberInput, Select

from django.forms import ModelForm
from product.models import Product
from django.forms import Select
# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    order_placed = models.BooleanField(default=False)
    # size = models.CharField(max_length=100,choices=SIZE, blank=True, null=True)
    size = models.CharField(max_length=10,blank=True, null=True)
    order_code = models.CharField(max_length=70, editable=False)

    

    @property
    def price(self):
        if self.product_id is not None:
            return (self.product.price)

    
    @property
    def amount(self):
        if self.product_id is None:
            return (None)
        else:
            if self.product.discount_price:
                return(self.product.discount_price * self.quantity)
            else:
                return(self.product.price * self.quantity)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity','size']


class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Accepted','Accepted'),
        ('preparing','prepating'),
        ('Onshipping','Onshipping'),
        ('completed','completed'),
        ('canceled','canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(blank=True, null=True)
    order_placed = models.BooleanField(default=False)
    order_code = models.CharField(max_length=70, editable=False)
    payment_code = models.CharField(max_length=8, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(blank=True, null=True,max_length=20)
    address = models.CharField(max_length=150,blank=True, null=True)
    city = models.CharField(blank=True,max_length=150)
    state = models.CharField(blank=True, null=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    

class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields = ['first_name','last_name','address','phone','city','country']