from django.contrib import admin

from .models import Customer, Service, Product


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'phone_number' )
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ( 'project_name', 'project_number', 'cust_name')
    list_filter = ( 'project_name', 'project_number')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'pickup_time')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)
