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

    @staticmethod
    def get_absolute_url():
        return '/guestlist'


class Employee(models.Model):
    CON = 'CON'
    BH = 'BH'
    KIT = 'KIT'
    CUS = 'CUS'
    POSITION_CHOICES = [
        (CON, 'Concierge'),
        (BH, 'Bellhop'),
        (KIT, 'Kitchen'),
        (CUS, 'Custodial')
    ]
    first = models.CharField(max_length=100, default='')
    last = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=3, choices=POSITION_CHOICES, default=CON)
    ssn = models.CharField(max_length=12, default='')
    hourly_rate = models.FloatField(default=12.5)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.last}-{self.id}'

    @staticmethod
    def get_absolute_url():
        return '/employeelist'


class Stay(models.Model):
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.guestid.last} staying in {self.roomid.room_num} from {self.start} until {self.end}'
