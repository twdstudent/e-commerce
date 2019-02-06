from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

"""
TabularInline subclass defines the templates
used to render the order in the admin interface.
StackedInline is another option
"""
class OrderLineAdminInline(admin.TabularInline):
    models = OrderLineItem
    
"""
The admin interface has the abiltity to edit more
than one modelon on a single page.
This i sknown as inlines.
"""
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    
admin.site.register(Order, OrderAdmin)    