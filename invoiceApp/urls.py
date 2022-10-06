from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('invoices', views.invoices, name='invoices'),
    path('products', views.products, name='products'),
    path('clients', views.clients, name='clients'),

    path('invoice/create', views.createInvoice, name='create-invoice'),
    path('invoice/create-build/<slug:slug>/', views.createBuildInvoice, name='create-build-invoice'),
]