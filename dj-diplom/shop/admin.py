from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ShopUserCreationForm, ShopUserChangeForm
from .models import Item, Category, Review, Order, Shipping, ShopUser

# Register your models here.

class ShippingInline(admin.TabularInline):
    model = Shipping
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [ShippingInline]
    list_display = ('__str__', 'pub_date', 'user', 'items_count')
    list_filter = ['pub_date']


class ShopUserAdmin(UserAdmin):
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm
    model = ShopUser
    list_display = ['email', 'username',]


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)
admin.site.register(Shipping)
admin.site.register(ShopUser, ShopUserAdmin)