from django.contrib import admin
from .models import Station, Route

# Register your models here.


class StationAdmin(admin.ModelAdmin):
    pass


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)