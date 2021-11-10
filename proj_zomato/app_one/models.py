from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.
class UserModel(models.Model):
    name=models.CharField(max_length=80)
    username=models.CharField(max_length=80)
    password=models.CharField(max_length=10)
    user_type=models.CharField(max_length=50,null=True,blank=True)

class DishModel(models.Model):
    dish_name=models.CharField(max_length=30)
    dish_price=models.IntegerField()
    rest_available=models.CharField(max_length=60)

class RestaurantModel(models.Model):
    rest_name=models.CharField(max_length=50)
    rest_address=models.CharField(max_length=150)

class PlaceOrderModel(models.Model):
    user_order=models.CharField(max_length=80)
    rest_placed=models.CharField(max_length=50)
    dish_placed=models.CharField(max_length=30)
    total_price=models.IntegerField()
    date=models.DateTimeField()