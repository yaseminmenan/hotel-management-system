from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForm
from hotel_management_sys.functions.booking_availability import is_available


# Create your views here.
def homepage(request):
    all_rooms_qs = Room.objects.all()

    return render(request, 'homepage.html', {
        'name': 'Django',
        'rooms': all_rooms_qs
    })


class RoomList(ListView):
    model = Room


class BookingList(ListView):
    model = Booking


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'booking_form.html'

    def make_booking(self, room, data):
        booking = Booking.objects.create(
            user=self.request.user,
            room=room,
            check_in=data['check_in'],
            check_out=data['check_out']
        )
        booking.save()
        return booking

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(type=data['room_type'])

        for room in room_list:
            if is_available(room, data['check_in'], data['check_out']):
                booking = self.make_booking(room, data)
                return HttpResponse(booking)

        return HttpResponse('We are sorry, but all rooms of this type are fully booked.')