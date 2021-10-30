from django import forms
from .models import Guest, Employee, Stay


class GuestCreateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')


class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first', 'last', 'ssn', 'position', 'hourly_rate', 'hire_date')


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first', 'last', 'ssn', 'position', 'hourly_rate', 'hire_date')


class StayCreateForm(forms.ModelForm):
    class Meta:
        model = Stay
        fields = ('roomid', 'guestid', 'empid', 'start', 'end')
