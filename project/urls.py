"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/`
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
    path('shkprdash/', views.shkprdash, name='shkprdash'),
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
    path('product/', views.product, name='product'),
    path('allproduct/', views.allproduct, name='allproduct'),
   
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('profile/', views.profile, name='profile'),
    path('chat_list/', views.chat_list, name='chat_list'),
    path('logout/', views.logout, name='logout'),
    # path('cuschats/', views.cuschats, name='cuschats'),


    
    path('chat/', views.chat, name='chat'),
    path('buy_now/', views.buy_now, name='buy_now'),
    path('sort/', views.sort, name='sort'),

    path('chat/<str:other_user>/<int:product_id>/', views.chat_page, name='chat_page'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)