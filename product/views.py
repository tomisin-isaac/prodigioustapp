from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product(request):
    return HttpResponse('Hey world')
    # return render(request,'index.html')