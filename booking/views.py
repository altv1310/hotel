from django.shortcuts import render

# Create your views here.
ROOMS = [101, 102, 103, 104]


def home(request):
    return render(request, 'booking/home.html', context={
        'user_name': 'Steve',
        'available_rooms': ROOMS
    })
