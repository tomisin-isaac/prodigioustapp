from django.contrib import admin
from.models import *
# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('order_code','user','product','quantity','size','price','amount','order_placed')
    list_filter = ('user',)
    list_display_links =('order_code','user','product','quantity','size','price','amount','order_placed')
    can_delete = False


class OrderAdmin(admin.ModelAdmin):
    list_display =('order_code','user','order_placed','payment_code','total','created_at')
    # list_filter =('status',)
    list_display_links =('user',)
    readonly_fields = ('order_code','user','order_placed','payment_code','total','created_at')
    can_delete = False

    
admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)