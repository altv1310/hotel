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


class Guest(models.Model):
    MR = 'MR'
    MS = 'MS'
    DR = 'DR'
    OT = 'OT'
    HONORIFIC_CHOICES = [
        (MR, 'Mr.'),
        (MS, 'Ms.'),
        (DR, 'Dr.'),
        (OT, 'Other')
    ]
    honorific = models.CharField(max_length=2, choices=HONORIFIC_CHOICES, default=OT)
    first = models.CharField(max_length=100, default='')
    last = models.CharField(max_length=100, default='')
    vip = models.IntegerField(default=-1)
    email = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.first} {self.last}'
