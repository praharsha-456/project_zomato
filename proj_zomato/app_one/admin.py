from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserModel)
admin.site.register(DishModel)
admin.site.register(RestaurantModel)
admin.site.register(PlaceOrderModel)