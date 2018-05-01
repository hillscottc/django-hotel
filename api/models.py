from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    num_rooms = models.IntegerField(default=100)
    res_buffer = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=254, null=True)
    res_date = models.DateField('Date of the stay.')
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} at {} for {}".format(
            self.res_date.strftime("%Y-%m-%d"),
            self.hotel.name,
            self.client_name
        )
