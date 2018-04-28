from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Hotel

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
    return HttpResponse("You're reserving for hotel %s." % hotel_id)

