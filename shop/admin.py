from django.contrib import admin
from .models import Product, Category, A_size, A_image, A_color


@admin.register(A_size)
@admin.register(A_image)
@admin.register(A_color)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_price', 'price', 'category', 'seller', 'in_stock', 'slug', 'brand',
                    'display_image',
                    'created', 'updated']
    list_editable = ['discount_price', 'price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}
