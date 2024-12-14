from django.contrib import admin
from .models import IceCream

# Register your models here.


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor', 'price', 'available', 'created_at')
    list_filter = ('flavor', 'available')
    search_fields = ('name',)
    ordering = ('-created_at',)
