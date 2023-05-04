from django.utils import timezone
from django.db import models

class books(models.Model):
    authorname=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    title=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    cover_page=models.FileField(upload_to='coverpages')
    file=models.FileField(upload_to='pdf')
    rating=models.IntegerField(default=0)
    hitrate=models.IntegerField(default=0)
    onestar=models.IntegerField(default=0)
    twostar=models.IntegerField(default=0)
    threestar=models.IntegerField(default=0)
    fourstar=models.IntegerField(default=0)
    fivestar=models.IntegerField(default=0)
    avgrating=models.FloatField(default=0.0)
    oneper=models.IntegerField(default=0)
    twoper=models.IntegerField(default=0)
    threeper=models.IntegerField(default=0)
    fourper=models.IntegerField(default=0)
    fiveper=models.IntegerField(default=0)



    def __str__(self):
        return f"{self.authorname} {self.email} {self.title}"
    
    def delete(self,*args,**kwargs):
        self.file.delete()
        self.cover_page.delete()
        super().delete(*args,**kwargs)


# Create your models here.

class readrate(models.Model):
    title=models.CharField(max_length=254)
    rating=models.IntegerField()
    hitrate=models.IntegerField()
    onestar=models.IntegerField()
    twostar=models.IntegerField()
    threestar=models.IntegerField()
    fourstar=models.IntegerField()
    fivestar=models.IntegerField()
    genre=models.CharField(max_length=254)
    date_time=models.DateTimeField(default=timezone.now)
