from django.contrib import admin
from myapp.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category_image')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
