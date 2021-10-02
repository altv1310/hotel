from django.db import models

BASE_PRICE = 200.00
SUITE_UPCHARGE = .25
OCEAN_UPCHARGE = .4


# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    occupied = models.BooleanField(default=False)
    oceanside = models.BooleanField(default=False)
    suite = models.BooleanField(default=False)
    if suite:
        price = models.FloatField(default=BASE_PRICE)

    def __str__(self):
        return f'Room#{self.room_num}'
