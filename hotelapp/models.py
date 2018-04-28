from django.db import models
from django.utils import timezone

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    res_buffer = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)    
    date_res = models.DateTimeField('Date of the stay.')
    date_updated = models.DateTimeField('Date res placed/updated.')

    def is_current(self):
        return self.date_res >= timezone.now()

    def __str__(self):
        return self.date_res + " at " + self.hotel + " for " + self.customer
