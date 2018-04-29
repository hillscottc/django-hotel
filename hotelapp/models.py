from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    num_rooms = models.IntegerField(default=100)
    res_buffer = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ReservationManager(models.Manager):
    def create_res(self, hotel, customer, date_res):
        res = self.create(hotel=hotel, customer=customer, date_res=date_res)
        return res
      

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)    
    date_res = models.DateField('Date of the stay.')
    date_updated = models.DateTimeField(auto_now=True)
    objects = ReservationManager()

    def is_current(self):
        return self.date_res >= timezone.now()

    def __str__(self):
        return self.date_res.strftime("%Y-%m-%d") + ' at ' + self.hotel.name + ' for ' + self.customer
