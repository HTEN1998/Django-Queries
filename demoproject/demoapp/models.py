from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    price = models.IntegerField()

class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    # customer_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    customer_loc = models.CharField(max_length=50)
