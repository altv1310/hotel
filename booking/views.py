from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Room, Guest, Employee
from .forms import GuestCreateForm, GuestUpdateForm, EmployeeCreateForm, EmployeeUpdateForm

# Create your views here.
ROOMS = [101, 102, 103, 104]


class GuestCreate(CreateView):
    model = Guest
    template_name = 'booking/guest_create_form.html'
    form_class = GuestCreateForm


class GuestUpdate(UpdateView):
    model = Guest
    template_name = 'booking/guest_update_form.html'
    form_class = GuestUpdateForm


class GuestDelete(DeleteView):
    model = Guest
    template_name = 'booking/guest_delete_form.html'
    success_url = '/guestlist'


class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'booking/employee_create_form.html'
    form_class = EmployeeCreateForm


class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'booking/employee_update_form.html'
    form_class = EmployeeUpdateForm


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'booking/employee_delete_form.html'
    success_url = '/employeelist'


class RoomList(ListView):
    model = Room


class GuestList(ListView):
    model = Guest


class EmployeeList(ListView):
    model = Employee


def home(request):
    return render(request, 'booking/home.html', context={
        'user_name': 'Steve',
        'available_rooms': ROOMS
    })
