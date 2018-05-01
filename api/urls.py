from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HotelList, HotelDetail, ReservationList, ReservationDetail


urlpatterns = [
    url(r'^hotels/$', HotelList.as_view()),
    url(r'^hotels/(?P<pk>[0-9]+)/$', HotelDetail.as_view()),
    url(r'^reservations/$', ReservationList.as_view()),
    url(r'^reservations/(?P<pk>[0-9]+)/$', ReservationDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
