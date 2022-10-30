from django.db import models

# Create your models here.
class Device(models.Model):
    type = models.CharField(max_length = 100,blank=False)
    price = models.IntegerField()
    choices = (
        ('AVAILABLE','Item ready to be purchased'),
        ('SOLD','Item Sold'),
        ('RESTOCKING','Item restocking in few days')
    )
    status = models.CharField(max_length=10,choices = choices, default="AVAILABLE") # Available ,sold,restocking
    # issues = models.CharField(max_length = 100,default = "no issues")

    class Meta:
        abstract = True   # this is done so that when migration script runs no table is created of this class

    def __str__(self):
        return 'Type:{0} Price : {1}'.format(self.type,self.price)


class Laptop(Device):
    pass   #SIMPLY INHERTING THE VALUES FROM DEVICES AND PASSING IT

class Mobile(Device):
    pass

class Desktop(Device):
    pass


