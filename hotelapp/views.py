from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world, from hotelapp index.")

def hotel_detail(request, hotel_id):
    return HttpResponse("You're looking at hotel %s." % hotel_id)

def hotel_reservations(request, hotel_id):
    response = "You're looking at the reservations of hotel %s."
    return HttpResponse(response % hotel_id)

def reserve(request, hotel_id):
    return HttpResponse("You're reserving for hotel %s." % hotel_id)

