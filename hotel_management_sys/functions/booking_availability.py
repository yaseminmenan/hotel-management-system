import datetime
from hotel_management_sys.models import Room, Booking


def is_available(room, check_in, check_out):
    room_bookings = Booking.objects.filter(room=room)

    for booking in room_bookings:
        if booking.check_in < check_out or booking.check_out > check_in:
            return False

    return True

