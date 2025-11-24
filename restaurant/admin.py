from django.contrib import admin
from .models import Restaurant, MenuItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "is_active", "created_at")
    search_fields = ("name", "phone")
    list_filter = ("is_active",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "restaurant", "price", "is_available")
    search_fields = ("name",)
    list_filter = ("is_available", "restaurant")
