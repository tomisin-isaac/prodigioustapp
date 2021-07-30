from django.contrib import admin
from.models import *

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id','title','company','status','icon','logo','menu_icon','cart_icon','banner_text')
    list_display_links = ['id','title','company']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','brands']

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['id','title','testimonials','comment']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','status','note')
    readonly_fields = ('name','subject','email','message')
    list_filter = ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email','subject','message','status','note')
    list_per_page = 20
# Register your models here.

admin.site.register(Setting,SettingAdmin)
admin.site.register(Brands,BrandAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)