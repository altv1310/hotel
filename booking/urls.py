from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roomlist', views.RoomList.as_view(), name='room_list'),
    path('guestlist', views.GuestList.as_view(), name='guest_list')
]
