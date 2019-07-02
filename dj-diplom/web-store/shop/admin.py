from django.contrib import admin
from .models import Item, Category, Review, Order, Shipping

# Register your models here.

class ShippingInline(admin.TabularInline):
    model = Shipping
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [ShippingInline]
    list_display = ('__str__', 'pub_date', 'user', 'items_count')
    list_filter = ['pub_date']


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)
admin.site.register(Shipping)