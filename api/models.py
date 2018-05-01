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
    def create_res(self, hotel, client_name, client_email, date_start, date_end):
        res = self.create(hotel=hotel, client_name=client_name, client_email=client_email,
                          date_start=date_start, date_end=date_end)
        # call validation
        # res.full_clean()
        return res


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=254, null=True)
    res_date = models.DateField('Date of the stay.')
    date_updated = models.DateTimeField(auto_now=True)
    objects = ReservationManager()

    def __str__(self):
        return "{} at {} for {}".format(
            self.res_date.strftime("%Y-%m-%d"),
            self.hotel.name,
            self.client_name
        )