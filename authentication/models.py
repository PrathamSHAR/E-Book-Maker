
from django.utils import timezone
from django.db import models


# Create your models here.
class Onetimepassword(models.Model):
    otp_num=models.IntegerField()
    username=models.CharField(max_length=50)
    date_time=models.DateTimeField(default=timezone.now)


class Verifytable(models.Model):
   otp_num=models.IntegerField()
   username=models.CharField(max_length=50)
   date_time=models.DateTimeField(default=timezone.now)
   
    
