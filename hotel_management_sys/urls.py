from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView, about, homepage, services
from allauth.account.views import LoginView, LogoutView
app_name = "hotel_management_sys"

urlpatterns = [
    path('', homepage, name='Home'),
    path('about/', about, name='About'),
    path('services/', services, name='Services'),
    path('room_list/', RoomListView, name='RoomListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<type>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),
    path('login/', LoginView.as_view(), name='LoginView'),
    path('logout/', LogoutView.as_view(), name='LogoutView'),
]