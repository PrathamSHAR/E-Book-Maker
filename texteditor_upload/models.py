from django.utils import timezone
from django.db import models

class books(models.Model):
    authorname=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    title=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    cover_page=models.FileField(upload_to='coverpages')
    file=models.FileField(upload_to='pdf')

    def __str__(self):
        return f"{self.authorname} {self.email} {self.title}"
    
    def delete(self,*args,**kwargs):
        self.file.delete()
        self.cover_page.delete()
        super().delete(*args,**kwargs)


# Create your models here.

class readrate(models.Model):
    title=models.CharField(max_length=254)
    rate=models.IntegerField()
    hitrate=models.IntegerField()
    date_time=models.DateTimeField(default=timezone.now)
