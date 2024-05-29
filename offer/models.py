from django.db import models
from store.models import Store

# Create your models here.
class Coupon(models.Model):
    PERCENT = "PERCENT"
    FIXED = "FIXED"
    DIS_TYPE_CHOICES = (
        (PERCENT,PERCENT),
        (FIXED,FIXED),
    )
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='store_offer')
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True,blank=True)
    order_number = models.IntegerField(null=True,blank=True)
    discount_type = models.CharField(max_length=10,default=PERCENT,choices=DIS_TYPE_CHOICES)
    min_value = models.FloatField(default=0.0)
    max_value = models.FloatField(default=5000.0)
    total_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
