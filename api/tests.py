from django.test import TestCase
from api.models import Hotel, Reservation
from api.serializers import ReservationSerializer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class HotelTestCase(TestCase):
    def test_hotel_create(self):
        """Hotel can be created"""
        Hotel.objects.create(name="Test Hotel 1", num_rooms=4, res_buffer=1)
        hotel = Hotel.objects.get(name="Test Hotel 1")
        self.assertEqual(hotel.num_rooms, 4)

    def test_max_rooms(self):
        """max rooms = num + buf/100"""
        Hotel.objects.create(name="Test Hotel 1", num_rooms=2, res_buffer=50)
        hotel = Hotel.objects.get(name="Test Hotel 1")
        self.assertEqual(hotel.max_rooms, 3)


def get_reservation_serializer(reservation):
    serializer = ReservationSerializer(reservation)
    content = JSONRenderer().render(serializer.data)
    stream = BytesIO(content)
    data = JSONParser().parse(stream)
    return ReservationSerializer(data=data)


class ReservationTestCase(TestCase):

    def test_reservation_create(self):
        """Reservation can be created"""
        hotel = Hotel.objects.create(name="Test Hotel 1", num_rooms=3, res_buffer=1)
        reservation = Reservation.objects.create(hotel=hotel,
                                                 client_name="Smith",
                                                 start_date="2020-01-01",
                                                 end_date="2020-01-07")
        self.assertEqual(reservation.client_name, "Smith")

    def test_overbook(self):
        """
        Reservation overbook check via serializer.
        """
        # hotel with max 3 rooms
        hotel = Hotel.objects.create(name="Test Hotel 1", num_rooms=2, res_buffer=50)
        d = {'hotel': hotel, 'client_name': 'Smith',
             'start_date': "2020-01-01", 'end_date': '2020-01-01'}
        Reservation.objects.create(**d)
        Reservation.objects.create(**d)

        # Third room is ok
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), True)
        reservation.save()

        # Four is too many
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)

        # One of the dates is the range is still invalid
        d = {'hotel': hotel, 'client_name': 'Smith',
             'start_date': "2019-12-31", 'end_date': '2020-01-02'}
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)

        # Can still book other dates
        d = {'hotel': hotel, 'client_name': 'Smith',
             'start_date': "2020-02-01", 'end_date': '2020-02-07'}
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), True)
        reservation.save()

    def test_bad_end_date(self):
        """
        End date cannot be before the start date
        """
        hotel = Hotel.objects.create(name="Test Hotel 1", num_rooms=3, res_buffer=1)
        d = {'hotel': hotel, 'client_name': 'Smith',
             'start_date': "2020-02-01",
             'end_date': '1999-01-01'}
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)

    def test_past_date(self):
        """
        Can't book dates in the past
        """
        hotel = Hotel.objects.create(name="Test Hotel 1", num_rooms=3, res_buffer=1)
        d = {'hotel': hotel, 'client_name': 'Smith',
             'start_date': "1999-01-01",
             'end_date': '1999-01-02'}
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)