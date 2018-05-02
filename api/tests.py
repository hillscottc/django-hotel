from django.test import TestCase
from rest_framework import serializers
from api.models import Hotel, Reservation
from api.serializers import ReservationSerializer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


def get_serializer(reservation):
    serializer = ReservationSerializer(reservation)
    content = JSONRenderer().render(serializer.data)
    stream = BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = ReservationSerializer(data=data)
    return serializer


class HotelTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(name="Test Hotel 1", num_rooms=4, res_buffer=1)

    def test_hotel_create(self):
        """Hotel can be created"""
        hotel = Hotel.objects.get(name="Test Hotel 1")
        self.assertEqual(hotel.num_rooms, 4)


class ReservationTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(name="Test Hotel 1", num_rooms=4, res_buffer=1)
        Hotel.objects.create(name="Test Hotel 2", num_rooms=1, res_buffer=1)

    def test_reservation_create(self):
        """Reservation can be created"""
        hotel = Hotel.objects.get(name="Test Hotel 1")
        reservation = Reservation.objects.create(hotel=hotel,
                                                 client_name="Smith",
                                                 res_date="2020-01-01")
        self.assertEqual(reservation.client_name, "Smith")

    def test_overbook(self):
        """Reservation overbook check via serializer"""
        hotel = Hotel.objects.get(name="Test Hotel 2")
        reservation = Reservation(hotel=hotel, client_name="Smith", res_date="2020-01-01")
        reservation.save()
        reservation = Reservation(hotel=hotel, client_name="Smith", res_date="2020-01-01")
        reservation.save()
        reservation = Reservation(hotel=hotel, client_name="Smith", res_date="2020-01-01")
        serializer = get_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)
