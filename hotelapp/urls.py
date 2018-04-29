from django.urls import path

from . import views

app_name = 'hotelapp'
urlpatterns = [
    # ex: /hotelapp/
    path('', views.index, name='index'),
    
    # ex: /hotelapp/5/
    path('<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    
    # ex: /hotelapp/5/reservations/
    path('<int:hotel_id>/reservations/', views.hotel_reservations, name='hotel_reservations'),
    
    # ex: /hotelapp/5/reserve/
    path('<int:hotel_id>/reserve/', views.reserve, name='reserve'),
]