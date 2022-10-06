from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *

from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4


#Anonymous required
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
    )

   if function:
       return actual_decorator(function)
   return actual_decorator


# Create your views here.
def index(request):
    return render(request, 'invoiceApp/index.html')


@anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'invoiceApp/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect('dashboard')
        else:
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'invoiceApp/login.html', context)

# def login(request):
#     form = UserLoginForm
#     return render(request, 'invoiceApp/login.html', {
#         'form': form,
#     })

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'invoiceApp/dashboard.html')

@login_required
def invoices(request):
    context = {}
    invoices = Invoice.objects.all()
    context['invoices'] = invoices
    return render(request, 'invoiceApp/invoices.html', context)


@login_required
def products(request):
    context = {}
    return render(request, 'invoiceApp/products.html')


@login_required
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm2()
        context['form'] = form
        return render(request, 'invoiceApp/clients.html', context)

    if request.method == 'POST':
        form = ClientForm2(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('clients')

    return render(request, 'invoiceApp/clients.html', context)

    ##------------------ Create Invoice Views Start here ------------------##

@login_required
def createInvoice(request):
    number =    "INV-" + str(uuid4()).split('-')[1]
    newInvoice = Invoice.objects.create(number=number) 
    newInvoice.save()
    inv = Invoice.objects.get(number=number)

    return redirect('create-build-invoice', slug=inv.slug)
    

@login_required
def createBuildInvoice(request, slug):# fetch that invoice
    #invoice = Invoice.objects.get(slug=slug) i'll user try catch
    try:
        invoice = Invoice.objects.get(slug=slug) 
        pass
    except: 
        messages.error(request, 'something went wrong.')
        return redirect('invoices')
    

    # fetch all the product related to this invoice
    products = Product.objects.filter(invoice=invoice)

    context = {}
    context['invoice'] = invoice
    context['products'] = products

    if request.method == 'GET':
        prod_form = ProductForm()
        inv_form = InvoiceForm()
        context['prod_form'] = prod_form
        context['inv_form'] = inv_form
        return render(request, 'invoiceApp/create-invoice.html', context)

    return render(request, 'invoiceApp/create-invoice.html', context)