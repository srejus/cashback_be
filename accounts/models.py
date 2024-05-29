from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15,null=True,blank=True)
    otp = models.IntegerField(null=True,blank=True)
    otp_created_at = models.DateTimeField(null=True,blank=True)
    place = models.CharField(max_length=150,null=True,blank=True)
    referral_code = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return str(self.full_name)
