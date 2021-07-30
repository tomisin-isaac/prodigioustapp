"""prodigiousapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from user.forms import RegisterForm
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from user import views as UserViews
urlpatterns = [
    path('',include('home.urls')),
    path('product/',include('product.urls')),
    path('user/',include('user.urls')),
    path('accountform/', UserViews.accountform, name='accountform'),
    path('login/', UserViews.loginform, name='loginform'),
    path('logout/', UserViews.logoutfunc,name='logoutfunc'),
    path('register/', UserViews.registerform,name='registerform'),
    path('update/', UserViews.userupdate, name='userupdate'),
    path('password/', UserViews.userpassword,name='userpassword'),
    path('order/',include('order.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
