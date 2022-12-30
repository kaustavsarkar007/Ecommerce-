from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('processorder', views.processOrder, name="processOrder"),
    path('contact/', views.contact, name='contact'),
    path('signup', views.handleSignup, name='handlesignup'),
    path('login', views.handleLogin, name='handlelogin'),
    path('logout', views.handleLogout, name='handlelogout'),
]