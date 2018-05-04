from rest_framework import generics
from .serializers import HotelSerializer, ReservationSerializer
from .models import Hotel, Reservation


class HotelList(generics.ListCreateAPIView):
    """
    List all hotels, or create a new hotel.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a hotel instance.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    
class ReservationList(generics.ListCreateAPIView):
    """
    List all reservations, or create a new reservation.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    
class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a reservation instance.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer