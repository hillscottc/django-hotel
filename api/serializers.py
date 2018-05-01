from rest_framework import serializers
from .models import Hotel, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'num_rooms', 'res_buffer')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'hotel', 'client_name', 'client_email', 'res_date')