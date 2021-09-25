from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'booking/home.html', context={
        'user_name': 'Steve',
        'available_rooms': [101, 102, 103, 104]
    })
