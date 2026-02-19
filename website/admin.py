from django.contrib import admin
from .models import RestaurantInfo

# Register your models here.


class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_details', 'opening_hours')


admin.site.register(RestaurantInfo, RestaurantInfoAdmin)
