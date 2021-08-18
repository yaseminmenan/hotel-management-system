from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from .models import Room, Booking
from .forms import AvailabilityForm
from django.urls import reverse, reverse_lazy
from hotel_management_sys.functions.booking_availability import is_available


# Create your views here.
def homepage(request):
    all_rooms_qs = Room.objects.all()

    return render(request, 'homepage.html', {
        'name': 'Django',
        'rooms': all_rooms_qs
    })


def about(request):
    return render(request, 'about.html', {
    })


def services(request):
    return render(request, 'services.html', {
    })


def RoomListView(request):
    room = Room.objects.all()[0]
    room_types = dict(room.ROOM_TYPES)

    room_list = []
    for room_type in room_types:
        room = room_types.get(room_type)
        room_url = reverse('hotel_management_sys:RoomDetailView', kwargs={'type': room_type})
        room_list.append((room, room_url))

    return render(request, 'room_list_view.html', {
        'room_list': room_list
    })


class BookingListView(ListView):
    model = Booking
    template_name = "booking_list_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list

        booking_list = []
        if self.request.user.is_anonymous:
            return booking_list

        booking_list = Booking.objects.filter(user=self.request.user)
        return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        room_type = self.kwargs.get('type', None)
        room_list = Room.objects.filter(type=room_type)
        form = AvailabilityForm()

        if len(room_list) > 0:
            room = room_list[0]
            room_type = dict(room.ROOM_TYPES).get(room.type, None)
            return render(request, 'room_detail_view.html', {
                'room_type': room_type
        })
        else:
            return HttpResponse('That room type does not exist')

    def post(self, request, *args, **kwargs):
        room_type = self.kwargs.get('type', None)
        room_list = Room.objects.filter(type=room_type)

        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            for room in room_list:
                if is_available(room, data['check_in'], data['check_out']):
                    booking = Booking.objects.create(
                        user=self.request.user,
                        room=room,
                        check_in=data['check_in'],
                        check_out=data['check_out']
                    )
                    booking.save()
                    return HttpResponse(booking)

            return HttpResponse('We are sorry, but all rooms of this type are fully booked.')
        else:
            return HttpResponse('Error! Invalid form.')


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('hotel_management_sys:BookingListView')
