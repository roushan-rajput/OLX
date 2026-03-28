"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('userdash/', views.userdash, name='userdash'),
    path('login/', views.login, name='login'),
    path('Register/', views.Register, name='Register'),
    path('reg_data/', views.reg_data, name='reg_data'),
    path('postyouradd/', views.postyouradd, name='postyouradd'),
    path('forgetpage/', views.forgetpage, name='forgetpage'),
    path('send_otp/', views.send_otp, name='send_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('resetpass/', views.resetpass, name='resetpass'),
    path('logindata/', views.logindata, name='logindata'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_pro/', views.add_pro, name='add_pro'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('profile/', views.profile, name='profile'),
    path('chats/', views.chats, name='chats'),
    path('logout/', views.logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)