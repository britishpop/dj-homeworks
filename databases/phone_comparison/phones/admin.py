from django.contrib import admin
from .models import Chinaphone, Iphone

# Register your models here.

@admin.register(Chinaphone)
class ChinaphoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Iphone)
class IphoneAdmin(admin.ModelAdmin):
    pass