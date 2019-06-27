from django.contrib import admin
from .models import TableField, TableFile

# Register your models here.

class TableFieldAdmin(admin.ModelAdmin):
    pass


class TableFileAdmin(admin.ModelAdmin):
    pass


admin.site.register(TableField, TableFieldAdmin)
admin.site.register(TableFile, TableFileAdmin)