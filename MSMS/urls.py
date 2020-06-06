"""MSMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mobsms import views as mobsms_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mobsms_views.index,name='home'),
    path('register/',mobsms_views.regester,name='register'),
    path('quickview/<int:Id>',mobsms_views.quickView,name='quick view'),
    path('profile/',mobsms_views.profile,name='profile'),
    path('checkout/',mobsms_views.checkOut,name='check out'),
    path('addphone/',mobsms_views.add,name='add phone'),
    path('checkout/bill/<int:Id>',mobsms_views.bill,name='bill'),
    path('update/<int:Id>',mobsms_views.updateMobile,name='update mobile'),
    path('login/',auth_views.LoginView.as_view(template_name='mobsms/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='mobsms/logout.html'),name='logout')
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
