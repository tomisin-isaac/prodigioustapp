from django.core import paginator
from product.models import Product
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from user.models import UserProfile

from.models import *
from product.models import *
# from user.models import Userprofile


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    brands = Brands.objects.all()
    banner = Product.objects.get(banner=True)
    offer = Product.objects.get(offer=True)
    category = Category.objects.all()[:3]
    featured = Product.objects.filter(featured=True)
    latest = Product.objects.filter(latest=True)[:4]
    latest2 = Product.objects.filter(latest=True).order_by('-id')[:4]
    testimonials = Testimonials.objects.all()
    context ={
        'setting':setting,
        'brands':brands,
        'banner':banner,
        'offer':offer,
        'category':category,
        'featured':featured,
        'latest':latest,
        'latest2':latest2,
        'testimonials':testimonials,
    }
    return render(request, 'index.html',context)

def about(request):
    setting = Setting.objects.get(pk=1)
    testimonials = Testimonials.objects.all()
    context={
        'setting':setting,
        'testimonials':testimonials,
    }
    
    return render(request,'about.html',context)
    


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been sent! our customer serverce Team would be with you shortly')
            return redirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    brands = Brands.objects.all()
    category = Category.objects.all()

    context={
        'setting':setting,
        'form':form,
        'brands': brands,
        'category': category,
    }
    
    return render(request,'contact.html',context)


def category(request):
    setting = Setting.objects.get(pk=1)
    brands = Brands.objects.all()
    offer = Product.objects.get(offer=True)
    category = Category.objects.order_by('-created_at').filter(status=True)
    paginator = Paginator(category,4)
    page = request.GET.get('page')
    paged_category = paginator.get_page(page)

    
    context= {
        'setting':setting,
        'brands': brands,
        'offer':offer,
        'category':  paged_category,
    }

    return render(request, 'category.html',context)

def product_list(request,id,slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category__id=id)
    paginator = Paginator(products,4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    


    context={
        'setting':setting,
        'category':category,
        'catdata':catdata,
        'products':paged_products,
    }
    return render(request,'product.html',context)

def product_details(request,id,slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products = Product.objects.filter(category__id=id)
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)


    context={
        'setting':setting,
        'category':category,
        'products':products,
        'product':product,
        'images':images,
    }

    return render(request,'product-details.html',context)