from django.db import models
from random import randint
from datetime import datetime
from portal_official.models import official_athorities_list

# Create your models here.
class Portal_user(models.Model):
    login = models.CharField(max_length=50,primary_key=True)
    otp = models.CharField(max_length=5)
    otp_generated = models.TextField()
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.login

class Portal_user_profile(models.Model):
    login = models.ForeignKey(Portal_user,on_delete=models.CASCADE)
    localbody = models.ForeignKey(official_athorities_list, on_delete=models.CASCADE)

    fname = models.CharField(max_length=32,null=True)
    lname = models.CharField(max_length=32,null=True)
    email = models.CharField(max_length=32,null=True)
    altno = models.CharField(max_length=32,null=True)
    address = models.CharField(max_length=32,null=True)
    place = models.CharField(max_length=32,null=True)
    city = models.CharField(max_length=32,null=True)
    pincode = models.CharField(max_length=6,null=True)


    def __str__(self):
        return str(self.login)

class food_item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=32)
    item_description = models.TextField(null=True)
    item_price = models.FloatField()
    item_qty = models.IntegerField(default=0)
    item_date = models.TextField(null=True)
    localbody = models.ForeignKey(official_athorities_list,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return ("%s - %s "%(self.item_name,self.localbody))

class food_item_list_in_orders(models.Model):
    item_id = models.ForeignKey(food_item,on_delete=models.CASCADE)
    item_qty = models.IntegerField()
    item_date = models.TextField(null=True)
    uid = models.TextField(default="0")
    user = models.CharField(max_length=10,default="0")
    localbody = models.ForeignKey(official_athorities_list,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "(%s) %s - %s" %(self.item_qty,self.item_id,self.uid)
class foods_order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.TextField(null=True)
    total_price = models.FloatField()
    user_id = models.ForeignKey(Portal_user_profile,on_delete=models.CASCADE)
    localbody = models.ForeignKey(official_athorities_list,on_delete=models.CASCADE,null=True)
    status = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    #items_ordered = models.OneToOneField(food_item_list_in_orders,on_delete=models.CASCADE)
    uid = models.TextField(default="0")
    def __str__(self):
        return "%s - %s %s %s" %(self.order_id,self.order_date,self.user_id,self.uid)

