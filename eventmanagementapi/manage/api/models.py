from django.db import models

# Create your models here.

#Creating Event Model

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('Formal','Formal'),
                           ('Casual','Casual'),
                           
                           ))
    added_date=models.DateTimeField(auto_now=True)
    #Date = models.DateField(default=Date)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +'--'+ self.location
    
    
    
#User Model
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)

    