from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    ordering = ['id']
    search_fields = ['brand', 'model']
    list_filter = ['brand', 'model']
    list_display = ['brand', 'model', 'review_count']


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    ordering = ['id']
    search_fields = ['car__brand', 'title']
    list_filter = ['car__brand']
    list_display = ['car', 'title']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
