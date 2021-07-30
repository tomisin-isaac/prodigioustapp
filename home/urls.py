from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=('index')),
    path('about/',views.about,name=('about')),
    path('contact/',views.contact,name=('contact')),

    path('category/',views.category,name='category'),
    path('product/<str:id>/<slug:slug>',views.product_list,name='product_list'),
    path('product-details/<str:id>/<slug:slug>',views.product_details,name='prod_details')
]
