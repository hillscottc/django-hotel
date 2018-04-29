from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Hotel, Reservation
import logging

logger = logging.getLogger(__name__)

def index(request):
    hotel_list = Hotel.objects.all()
    context = {'hotel_list': hotel_list}
    return render(request, 'hotelapp/index.html', context)

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotelapp/hotel_detail.html', {'hotel': hotel})    

def hotel_reservations(request, hotel_id):
    response = "You're looking at the reservations of hotel %s."
    return HttpResponse(response % hotel_id)

def reserve(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    date_res = request.POST['date_res']
    customer = request.POST['customer']

    # days_res = Reservation.objects.filter(date_res=date_res, hotel=hotel)
    # logger.info('days_res = ' + str(days_res.count()) )


    reservation = Reservation.objects.create_res(hotel, customer, date_res)
    return HttpResponseRedirect(reverse('hotelapp:hotel_detail', args=(hotel.id,)))

