from django.urls import path
from .views import RoomList, BookingList, BookingView

app_name='hotel_management_sys'

urlpatterns=[
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView')
]