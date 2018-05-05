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
    start_date = models.DateField('Start of the stay.')
    end_date = models.DateField('End of the stay.')
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} to {} at {} for {}".format(
            self.start_date.strftime("%Y-%m-%d"),
            self.end_date.strftime("%Y-%m-%d"),
            self.hotel.name,
            self.client_name
        )
