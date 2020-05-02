from django.contrib import admin
from .models import Portal_user,Portal_user_profile,food_item,foods_order,food_item_list_in_orders
# Register your models here.
admin.site.register(Portal_user)
admin.site.register(Portal_user_profile)
admin.site.register(food_item)
admin.site.register(foods_order)
admin.site.register(food_item_list_in_orders)