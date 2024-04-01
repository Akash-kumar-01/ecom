"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/<str:gen>/<str:sc>/<str:br>/',views.shop),
    path('product/<int:id>/',views.product),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('sellerprofile/',views.sellerprofile),
    path('updateprofile/',views.updateprofile),
    path('addproduct/',views.addproduct),
    path('deleteproduct/<int:num>/',views.deleteproduct),
    path('editproduct/<int:num>/',views.editproduct),
    path('buyerprofile/',views.buyerprofile),
    path('wishlist/<int:num>/',views.wishlistpage),
    path('deletewishlist/<int:num>/',views.deletewishlist),
    path('cart/',views.cartpage),
    path('deletecart/<int:id>/',views.deletecart),
    path('checkout/',views.checkout),
    path('confirm/',views.confirmationpage),
    path('forgetpassword/',views.forgetpassword),
    path('confirmotp/<str:username>/',views.confirmotp),
    path('enterpassword/<str:username>/',views.enterpassword),
    path('paymentsucesss/',views.paymentSuccesss),
    path('subscribe/',views.SubscribePage),
    path('contact/',views.Contactpage),
    path('deletecheckout/<int:num>/',views.deletecheckout),
    path('paynow/<int:num>/',views.paynow),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
