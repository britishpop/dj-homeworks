from django.contrib import admin
from .models import Phone, Chinaphone, Iphone

# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Chinaphone)
class ChinaphoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Iphone)
class IphoneAdmin(admin.ModelAdmin):
    pass