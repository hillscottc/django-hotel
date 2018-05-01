from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger('api')


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    num_rooms = models.IntegerField(default=100)
    res_buffer = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class OverbookError(Exception):
    logger.warn('Hotel is FULL for this day!')


class ReservationManager(models.Manager):
    def create_res(self, hotel, customer, date_res):
        res = self.create(hotel=hotel, customer=customer, date_res=date_res)
        # call validation
        # res.full_clean()
        return res


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    date_start = models.DateField('Start of the stay.')
    date_end = models.DateField('End of the stay.')
    date_updated = models.DateTimeField(auto_now=True)
    objects = ReservationManager()

    def __str__(self):
        return "{} to {} at {} for {}".format(
            self.date_start.strftime("%Y-%m-%d"),
            self.date_end.strftime("%Y-%m-%d"),
            self.hotel.name,
            self.customer
        )