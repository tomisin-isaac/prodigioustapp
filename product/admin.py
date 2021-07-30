from django.contrib import admin
from.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display =['id','title','status','image']
    list_filter = ['status']
    prepopulated_fields ={'slug':('title',)}


class ProductImageInline(admin.TabularInline):
    model = Images 
    extra = 4 

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','status','image','quantity_instock','available','banner','slug','offer']
    list_filter = ['category']
    list_display_links = ('title','category','status','image')
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug':('title',)}
    list_editable = ['banner','offer']


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)