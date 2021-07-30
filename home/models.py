from django.db import models

from django.forms import Textarea, TextInput
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Setting(models.Model):
    STATUS =(
        ('True','True'),
        ('False','False'),
    )

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    logo = models.ImageField(blank=True, null=True, upload_to='images/')
    cart_icon = models.ImageField(blank=True, null=True, upload_to='images/')
    menu_icon = models.ImageField(blank=True, null=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=100)
    instargram = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    about = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS)
    banner_text = RichTextUploadingField(default='what we do')

    def __str__(self):
        return self.title

class Brands(models.Model):
    title = models.CharField(max_length=10,blank=True,null=True)
    brands = models.ImageField(blank=True,null=True,upload_to='images/')

    def __str__(self):
        return self.title
    
class Testimonials(models.Model):
    title = models.CharField(max_length=10,blank=True,null=True)
    comment = models.CharField(max_length=250,blank=True,null=True,default='Thumbs up prodigious store')
    testimonials = models.ImageField(blank=True,null=True,upload_to='images/')

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS =(
        ('New','New'),
        ('Read','Read'),
        ('pending','pending'),
        ('Closed','Closed'),
    )

    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True, max_length=225)
    status = models.CharField(choices=STATUS, default='New', max_length=10)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.name
    

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','subject','message']    