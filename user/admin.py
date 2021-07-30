from django.contrib import admin

from.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display =['id','username','first_name','last_name','images','email','address','phone','city','country']
    # readonly_fields = ['id','username','first_name','last_name','images','email','address','phone','city','country']
# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)
