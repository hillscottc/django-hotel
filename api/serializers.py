from datetime import timedelta, date
from rest_framework import serializers
from .models import Hotel, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'num_rooms', 'res_buffer')


def daterange(start_date, end_date):
    """Iterate a range of dates"""
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


def validate_for_overbook(hotel, start_date, end_date):
    """
    Verify each day in the range is not overbooked
    """
    # print('VALIDATING {} to {}'.format(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
    for single_date in daterange(start_date, end_date):
        days_res = Reservation.objects.filter(start_date__gte=single_date,
                                              end_date__lte=single_date,
                                              hotel=hotel)
        # print('{} res on day {}'.format(days_res.count(), day.strftime("%Y-%m-%d")))
        if days_res.count() >= hotel.max_rooms:
            raise serializers.ValidationError(
                'Hotel is FULL on {}.'.format(single_date.strftime("%Y-%m-%d")))


class ReservationSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate(data):
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError('End date must be AFTER the start date.')

        if data['start_date'] < date.today() or data['end_date'] < date.today():
            raise serializers.ValidationError("Can't book days in the PAST.")

        validate_for_overbook(data['hotel'], data['start_date'], data['end_date'])
        return data

    class Meta:
        model = Reservation
        fields = ('id', 'hotel', 'client_name', 'client_email', 'start_date', 'end_date')
