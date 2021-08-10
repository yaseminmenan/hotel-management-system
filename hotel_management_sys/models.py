from django.db import models
from django.conf import settings


# Create your models here.
class MyModel(models.Model):
    class Meta:
        abstract = True


class Room(MyModel):
    class Meta:
        db_table = 'hotel_room'

    ROOM_TYPES = (
        ('SIN', 'Single'),
        ('DOU', 'Double'),
        ('TRI', 'Triple'),
        ('TWI', 'Twin')
    )

    number = models.IntegerField()
    type = models.CharField(max_length=3, choices=ROOM_TYPES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'Room {self.number} - {self.type} - {self.beds} beds - {self.capacity} persons'


class Booking(models.Model):
    class Meta:
        db_table = 'booking'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


