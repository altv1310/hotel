from django.shortcuts import render
from django.views.generic import ListView
from .models import Room, Guest


# Create your views here.
ROOMS = [101, 102, 103, 104]


class RoomList(ListView):
    model = Room


class GuestList(ListView):
    model = Guest


def home(request):
    return render(request, 'booking/home.html', context={
        'user_name': 'Steve',
        'available_rooms': ROOMS
    })
