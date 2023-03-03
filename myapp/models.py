from django.db import models
from django.utils import timezone


class students(models.Model):
    name=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Roll_No=models.IntegerField()
    Fees=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    address=models.CharField(max_length=100,default='')
    
    
    def __str__(self):
        return self.name
    

# Create your models here.
