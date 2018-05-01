from rest_framework import serializers
from .models import Hotel, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'num_rooms', 'res_buffer')


def can_book(hotel, res_date):
    """
    Don't allow too many for hotel day
    """
    days_res = Reservation.objects.filter(res_date=res_date, hotel=hotel)
    if days_res.count() >= (hotel.num_rooms + hotel.res_buffer):
        raise serializers.ValidationError('Hotel is FULL for this day.')


class ReservationSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate(data):
        can_book(data['hotel'], data['res_date'])
        return data

    class Meta:
        model = Reservation
        fields = ('id', 'hotel', 'client_name', 'client_email', 'res_date')