from django.contrib import admin
from collection.models import Collection, Category, Subcategory, Product
# Register your models here.


class CollectionAdmin(admin.ModelAdmin):
	list_display=('name','is_published')

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Category)


class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('name','parent','order')
	list_filter = ('parent',)
admin.site.register(Subcategory, SubcategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','category', 'subcategory', 'price', 'collection')
	list_filter = ('collection','category','subcategory')

admin.site.register(Product, ProductAdmin)