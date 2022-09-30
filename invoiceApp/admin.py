from django.contrib import admin

from invoiceApp.models import Customer, Invoice, InvoiceLine, Product, ProductCategorie, Client, Settings


# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(ProductCategorie)
admin.site.register(Invoice)
admin.site.register(InvoiceLine)
admin.site.register(Client)
admin.site.register(Settings)