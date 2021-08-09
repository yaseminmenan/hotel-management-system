from django.db import models


# Create your models here.
class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
