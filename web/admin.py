from django.contrib import admin
from . models import Product, LogoSectionProduct, Category
from django.contrib.auth.models import User, Group

# Register your models here.
# To remove user,groups from admin panel
# admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(LogoSectionProduct)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category", "name","price")
    list_filter = ("category",)
    search_fields = (
        "name",
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = (
        "name",
    )