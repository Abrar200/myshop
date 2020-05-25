"""myshop URL Configuration

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
from django.urls import path, include
from orders2 import views as orders_views
from orders2.views import OrderSummaryView, CheckoutView, PaymentView, AddCouponView, RequestRefundView
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_to_cart/<slug>/', orders_views.add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>/', orders_views.remove_from_cart, name='remove-from-cart'),
    path('update-qty', orders_views.update_qty, name='update-qty'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('remove_item_from_cart/<slug>/', orders_views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('login/', accounts_views.login_view, name='login'),
    path('account/', accounts_views.account, name='account'),
    path('register/', accounts_views.registration_view, name='register'),
    path('', include('products.urls'))
]
